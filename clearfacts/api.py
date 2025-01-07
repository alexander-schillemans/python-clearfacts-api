import requests
import json

from . import config
from .authhandler import AuthHandler
from .methods.users import UserMethods
from .methods.invoices import InvoiceMethods

class ClearFactsAPI:

    def __init__(self, token: str | None = None) -> None:
        self.token = token

        self.headers = {
            'Accept' : 'application/json',
            'Content-Type' : 'application/json',
        }

        self.base_url = config.BASE_URL
        self.oauth2_server_url = config.OAUTH2_SERVER_URL
        self.auth_handler = AuthHandler(self, token)

        self.users = UserMethods(self)
        self.invoices = InvoiceMethods(self)
    
    def do_request(self, method, url=None, data=None, headers=None, files=None, base=None):

        if headers:
            merged_headers = self.headers
            merged_headers.update(headers)
            headers = merged_headers
        else: headers = self.headers

        base = self.base_url if not base else base
        url = '{base}/{url}'.format(base=base, url=url) if url else base

        if method == 'GET':
            response = requests.get(url, params=data, headers=headers)
        elif method == 'POST':
            if files: response = requests.post(url, data=data, files=files, headers=headers)
            else: response = requests.post(url, data=json.dumps(data), headers=headers)

        return response

    def request(self, method, url=None, data=None, headers=None, files=None, base=None):

        # Checks if the Authorization header is present and set it if not
        self.auth_handler.check_header_tokens()

        response = self.do_request(method, url, data, headers, files, base)
        response_json_content = json.loads(response.content) if response.content else None

        return response.status_code, response.headers, response_json_content

    def get(self, url=None, data=None, headers=None, base=None):
        status, headers, response = self.request('GET', url, data, headers, base=base)
        return status, headers, response
    
    def post(self, url=None, data=None, headers=None, files=None, base=None):
        status, headers, response = self.request('POST', url, data, headers, files, base)
        return status, headers, response