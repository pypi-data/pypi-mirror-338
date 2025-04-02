#!/usr/bin/env python3

import atexit
import base64
import configparser
from datetime import datetime, timedelta, timezone
import json
import os
import http
import urllib.error
import requests
import urllib
from . import UBIQ_HOST
from .configuration import ubiqConfiguration
from .events import events, eventsProcessor, syncEventsProcessor

from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend

class credentialsInfo:

    def __init__(self, access_key_id, secret_signing_key, secret_crypto_access_key, host, config_file, library_label, config_obj, idp_username, idp_password):
        self.__access_key_id = access_key_id
        self.__secret_signing_key = secret_signing_key
        self.__secret_crypto_access_key = secret_crypto_access_key
        
        self.__idp_username = idp_username
        self.__idp_password = idp_password
        self.__initialized = False
        
        self.__idp_cert_base64 = None
        self.__idp_cert_expires = None
        self.__encrypted_private_key = None
        
        self.__host = host
        if (not self.__host.lower().startswith('http')):
            self.__host = "https://" + self.__host

        if (config_file != None and config_obj != None):
               raise RuntimeError("Either config_file or config_obj should be set, but not both.")

        if (config_obj != None):
            self.__configuration = config_obj
        else:
            self.__configuration = ubiqConfiguration(config_file)
        
        # Event Tracking
        self.__events = events(self, self.__configuration, library_label)
        if self.__configuration.get_event_reporting_synchronous():
            self.__eventsProcessor = syncEventsProcessor(self.__configuration, self.__events)
        else:
            self.__eventsProcessor = eventsProcessor(self.__configuration, self.__events)
            self.__eventsProcessor.start()

    def get_access_key_id(self):
        return self.__access_key_id
    access_key_id=property(get_access_key_id)

    def get_secret_signing_key(self):
        return self.__secret_signing_key
    secret_signing_key=property(get_secret_signing_key)

    def get_secret_crypto_access_key(self):
        return self.__secret_crypto_access_key
    secret_crypto_access_key = property(get_secret_crypto_access_key)

    def get_host(self):
        return self.__host
    host = property(get_host)

    def get_configuration(self):
        return self.__configuration
    configuration = property(get_configuration)
    
    def get_encrypted_private_key(self):
        return self.__encrypted_private_key
    encrypted_private_key = property(get_encrypted_private_key)
    
    def get_idp_cert_base64(self):
        return self.__idp_cert_base64
    idp_cert_base64 = property(get_idp_cert_base64)

    def set(self):
        return (
                # Traditional
                self.__access_key_id != None and 
                self.__secret_signing_key != None and 
                self.__secret_crypto_access_key != None and 
                self.__access_key_id.strip() != "" and 
                self.__secret_signing_key.strip() != "" and 
                self.__secret_crypto_access_key.strip() != ""
            ) or (
                # IDP
                self.__idp_password != None and 
                self.__idp_password != None
            )
            
    
    def add_reporting_user_defined_metadata(self, data):
        self.__events.add_user_defined_metadata(data)
    
    def get_copy_of_usage(self):
        return self.__events.list_events()
    
    def get_event_count(self):
        return self.__events.get_events_count()

    # Forward events to event queue
    def add_event(self, dataset_name, dataset_group_name, billing_action, dataset_type, key_number, count):
        return self.__events.add_event(self.__access_key_id, dataset_name, dataset_group_name, billing_action, dataset_type, key_number, count)
    
    # Manually trigger process events
    def process_events(self):
        return self.__eventsProcessor.process()
    
    ## IDP RELEVANT FUNCTIONS ##
    
    def get_oauth_token(self):
        config = self.__configuration
        provider = config.get_idp_provider()
        endpoint = config.get_idp_token_endpoint_url()

        query = {
            'client_id': config.get_idp_tenant_id(),
            'client_secret': config.get_idp_client_secret(),
            'username': self.__idp_username,
            'password': self.__idp_password,
            'grant_type': 'password'
        }
        if provider == 'okta':
            query['scope'] = 'openid offline_access okta.users.read okta.groups.read'
        elif provider == 'entra':
            query['scope'] = f'api://{config.get_idp_tenant_id()}/.default'
        else:
            raise RuntimeError(f'Unknown or no IDP provider specified: {provider} Check your configuration and try again.')
        
        resp = requests.post(
            endpoint,
            data=query,
            headers={
                'Accept': 'application/json',
                'Cache-control': 'no-cache',
                'Content-type': 'application/x-www-form-urlencoded',
            })

        if resp.status_code != http.HTTPStatus.OK:
            raise urllib.error.HTTPError(
                endpoint, resp.status_code, f'Status ({resp.status_code}) Unable to fetch token from {endpoint}',
                resp.headers, resp.content
            )
        else:
            return json.loads(resp.content.decode())
    
    def get_idp_token_and_cert(self):
        self.token = self.get_oauth_token()
        self.sso = self.get_sso(self.token['access_token'], self.csr)
        api_cert = x509.load_pem_x509_certificate(self.sso['api_cert'].encode('utf-8'))
        self.__idp_cert_base64 = base64.b64encode(self.sso['api_cert'].encode('utf-8')).decode('utf-8')
        self.__idp_cert_expires = api_cert.not_valid_after_utc - timedelta(minutes=1)

    def renew_idp_cert(self):
        if self.is_idp():
            if self.__idp_cert_expires < datetime.now(timezone.utc):
                self.get_idp_token_and_cert()
    
    # Required call if IDP mode
    # Sets up the handshake between IDP & Ubiq
    def init(self):       
        srsa_bytes = base64.b64encode(os.urandom(33))
        self.__secret_crypto_access_key = srsa_bytes.decode('utf-8')        
        key = rsa.generate_private_key(
            backend=crypto_default_backend(),
            public_exponent=65537,
            key_size=4096
        )
        
        private_key = key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(srsa_bytes)
        )
        
        csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
            x509.NameAttribute(NameOID.COMMON_NAME, base64.b64encode(os.urandom(18)).decode('utf-8')),
            x509.NameAttribute(NameOID.COUNTRY_NAME, 'US'),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, 'California'),
            x509.NameAttribute(NameOID.LOCALITY_NAME, 'San Diego'),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, 'Ubiq Security, Inc.'),
            x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, 'Ubiq Platform')
        ])).sign(key, hashes.SHA256())
        
        self.csr = csr.public_bytes(serialization.Encoding.PEM)
        
        self.get_idp_token_and_cert()
        
        self.__access_key_id = self.sso['public_value']
        self.__secret_signing_key = self.sso['signing_value']

        self.__encrypted_private_key = private_key.decode('utf-8')
        self.__initialized = True

    def get_sso(self, access_token, csr):
        url = f'{self.host}/{self.__configuration.get_idp_ubiq_customer_id()}/api/v3/scim/sso'
        resp = requests.post(
            url=url,
            data=json.dumps({'csr': csr.decode('utf-8')}),
            headers={
                'Authorization': f'Bearer {access_token}',
                'Accept': 'application/json',
                'Cache-control': 'no-cache',
                'content-type': 'application/json'
            }
        )
        
        if resp.status_code != http.HTTPStatus.OK:
            raise urllib.error.HTTPError(url, resp.status_code, f'Status {resp.status_code} Unable to validate token {url}')
        else:
            return json.loads(resp.content.decode())

    # Easy method for checking if running in IDP mode
    def is_idp(self):
        ret = self.__idp_username != None and len(self.__idp_username) > 0
        
        if (ret and not self.__initialized):
            raise RuntimeError(f'Credentials.init() has not been called or failed but is required when using IDP authentication')
        
        return ret
        
    ## END IDP RELEVANT FUNCTIONS ##

# TODO: Rename configCredentials and load_config_file cause they are confusing. (configurableCredentials? load_credentials_file?)
class configCredentials(credentialsInfo):

    def load_config_file(self, credentials_file, profile):
        config = configparser.ConfigParser(interpolation=None)
        config.read(credentials_file)

        # Create empty dictionaries for the default and supplied profile
        d = {}
        p = {}

        # get the default profile if there is one
        if (config.has_section('default')):
            d = config['default']

        # get the supplied profile if there is one
        if (config.has_section(profile)):
            p = config[profile]

        # Use given profile if it is available, otherwise use default.
        self.__access_key_id= p.get('access_key_id', d.get('access_key_id'))
        self.__secret_signing_key = p.get('secret_signing_key', d.get('secret_signing_key'))
        self.__secret_crypto_access_key = p.get('secret_crypto_access_key', d.get('secret_crypto_access_key'))
        self.__host = p.get('SERVER', d.get('SERVER', UBIQ_HOST))
        self.__idp_username = p.get('IDP_USERNAME', d.get('IDP_USERNAME'))
        self.__idp_password = p.get('IDP_PASSWORD', d.get('IDP_PASSWORD'))


    def __init__(self, credentials_file = None, profile = "default", config_file = None, library_label = None, config_obj = None,):
        self.__access_key_id = None
        self.__secret_signing_key = None
        self.__secret_crypto_access_key = None
        self.__host = None
        self.__idp_username = None
        self.__idp_password = None

        if (credentials_file == None):
            from os.path import expanduser
            home = expanduser("~")
            credentials_file = os.path.join(home, ".ubiq", "credentials")

        if os.path.exists(credentials_file):
            self.load_config_file(credentials_file, profile)

        credentialsInfo.__init__(self, self.__access_key_id , self.__secret_signing_key, self.__secret_crypto_access_key, self.__host, config_file, library_label, config_obj, self.__idp_username, self.__idp_password)

        if (not self.set()):
            if (self.__access_key_id == None or self.__access_key_id.strip() == ""):
               raise RuntimeError("Unable to open credentials file '{0}' or unable to find 'access_key_id' value in profile '{1}'.".format(credentials_file, profile))
            elif (self.__secret_signing_key == None or self.__secret_signing_key.strip() == ""):
               raise RuntimeError("Unable to open credentials file '{0}' or unable to find 'secret_signing_key' value in profile '{1}'.".format(credentials_file, profile))
            elif(self.__secret_crypto_access_key == None or self.__secret_crypto_access_key.strip() == ""):
               raise RuntimeError("Unable to open credentials file '{0}' or unable to find 'secret_crypto_access_key' value in profile '{1}'.".format(credentials_file, profile))


class credentials(credentialsInfo):

    def __init__(self, access_key_id = None, secret_signing_key = None, secret_crypto_access_key = None, host = UBIQ_HOST, config_file = None, library_label = None, config_obj = None, idp_username = None, idp_password = None):
        # If supplied value is None, use ENV variable, otherwise use supplied value.
        # If env value isn't set, use the supplied value anyways (None) but prevent an exception
        self.__access_key_id = (access_key_id, os.getenv('UBIQ_ACCESS_KEY_ID', access_key_id)) [access_key_id == None]
        self.__secret_signing_key = (secret_signing_key, os.getenv('UBIQ_SECRET_SIGNING_KEY', secret_signing_key)) [secret_signing_key == None]
        self.__secret_crypto_access_key = (secret_crypto_access_key, os.getenv('UBIQ_SECRET_CRYPTO_ACCESS_KEY', secret_crypto_access_key)) [secret_crypto_access_key == None]
        config_file = (config_file, os.getenv('UBIQ_CONFIGURATION_FILE_PATH', config_file)) [config_file == None]
        self.__host = (host, os.getenv('UBIQ_SERVER', host)) [host == None]
        self.__idp_username = (idp_username, os.getenv('IDP_USERNAME', idp_username))[idp_username == None]
        self.__idp_password = (idp_password, os.getenv('IDP_PASSWORD', idp_password))[idp_password == None]

        credentialsInfo.__init__(self, self.__access_key_id,
                                 self.__secret_signing_key,
                                 self.__secret_crypto_access_key, 
                                 self.__host,
                                 config_file,
                                 library_label,
                                 config_obj,
                                 self.__idp_username,
                                 self.__idp_password)
        
        if (not self.set()):
            if (self.__access_key_id == None or self.__access_key_id.strip() == ""):
               raise RuntimeError("Environment variable for 'UBIQ_ACCESS_KEY_ID' not set.")
            elif (self.__secret_signing_key == None or self.__secret_signing_key.strip() == ""):
               raise RuntimeError("Environment variable for 'UBIQ_SECRET_SIGNING_KEY' not set.")
            elif(self.__secret_crypto_access_key == None or self.__secret_crypto_access_key.strip() == ""):
               raise RuntimeError("Environment variable for 'UBIQ_SECRET_CRYPTO_ACCESS_KEY' not set.")
