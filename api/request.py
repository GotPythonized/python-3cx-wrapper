import logging
from . import constants
from .exceptions import request_error_msg
import requests
import getpass
import json
from .utils import make_payload
import sys




class Request:
    logger = logging.getLogger()
    auth = constants.Authentication()
    authed = auth.authed
    r = requests.Session()
    r.headers = constants.HEADERS 
    username = auth.username
    password = auth.password
    fqdn = auth.fqdn
    port = auth.port

    def __init__(self, fqdn=None, port=5001, username=None, password=None, ):
        self.port = port
        if username and not self.username:
            self.username = username
        if password and not self.password:
            self.password = password
        if fqdn and not self.fqdn:
            self.fqdn = fqdn

    def set_up(self):
        if not self.username:
            if not self.auth.username:
                self.username = input("Username: ")
            else:
                self.username = self.auth.username
        if not self.password:
            if not self.auth.username:
                self.username = getpass.getpass("Password: ")
            else:
                self.password = self.auth.password

        if not self.fqdn:
            if not self.auth.fqdn:
                self.fqdn = input("FQDN: ")
            else:
                self.fqdn = self.auth.fqdn

        if ":" in self.fqdn:
            self.fqdn, self.port = self.fqdn.split(":")

        setattr(self.auth, 'fqdn', self.fqdn)
        setattr(self.auth, 'port', self.port)
        setattr(self.auth, 'username', self.username)
        setattr(self.auth, 'password', self.password)


        self.authed = True
        response = self.post('login', {'username': self.username, 'password': self.password})
            

    def get(self,request):
        if self.authed == False:
            self.set_up()
        response = self.r.get(constants.API_URL.format(self.fqdn, self.port,request), timeout=10)
        return self.prepare_response(response, request)
    
    def post(self, request, payload, files=None, timeout=5):
        if self.authed == False:
            self.set_up()

        self.r.headers['content-type'] =  "application/json;charset=UTF-8"
        if files:
            self.r.headers["DNT"] = "1"
        if isinstance(payload, dict):
            payload = json.dumps(payload)
        response = self.r.post(url=constants.API_URL.format(self.fqdn, self.port, request), data=payload, timeout=timeout)
        if response.status_code == 522:
            self.logger.debug(" *********************** " ,response.request.__dict__)
        return self.prepare_response(response, payload=payload)   
    
    def save(self, id):
        return self.post('edit/save', id)

    def update(self, id, key, value):
        return self.post('edit/update', make_payload(id, key, value))
        
    def prepare_response(self, response, request=None, payload=None):
        if response.status_code == 200:
            if response.headers.get('Set-Cookie'):
                self.logger.info(f"{response.request.method} {response.request.url} {response.status_code}")
                if "AuthSuccess" in response.text:
                    self.logger.info(f"Login Successful")
                    self.auth.Cookie = response.headers.get('Set-Cookie')
                    self.authed = True
            return response  
        else:
            self.logger.debug(response.reason, response.status_code, response.text)
            raise request_error_msg(response, payload)

request = Request