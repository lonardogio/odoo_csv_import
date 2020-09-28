import json
import random
import requests
import configparser as ConfigParser

SERVER_URL = 'http://localhost:8069'
DB_NAME = 'synclinic'
USERNAME = 'admin'
PASSWORD = 'odoo'


class JsonRpcOperation:
    server_url = ""
    db_name = ""
    username = ""
    password = ""

    def __init__(self, server_url=SERVER_URL, db_name=DB_NAME, username=USERNAME, password=PASSWORD):
        self.server_url = server_url
        self.db_name = db_name
        self.username = username
        self.password = password

    def _get_json_endpoint(self):
        json_endpoint = "%s/jsonrpc" % self.server_url
        return json_endpoint

    def _get_headers(self):
        headers = {"Content-Type": "application/json"}
        return headers

    def _authentication_op(self, odoo_model, op):
        """
            jsonrpc authentication
            :param odoo_model : odoo model for which authentication is assessed
            :param op : operation for which authentication is assessed (create, write, unlink)
            :return res['result'] : it says if the authentication was successful for a certain operation
        """
        payload = self._get_json_payload("common", "login", self.db_name, self.username, self.password)
        json_endpoint = self._get_json_endpoint
        headers = self._get_headers()
        response = requests.post(json_endpoint, data=payload, headers=headers)
        user_id = response.json()['result']

        res = None
        if user_id:
            payload = self._get_json_payload("object", "execute_kw", self.db_name, user_id, self.password,
                                             odoo_model, 'check_access_rights', [op])
            res = requests.post(json_endpoint, data=payload, headers=headers).json()
            print("Has " + str(op) + " access:" + res['result'])
        return res['result']

    def _get_json_payload(self, service, method, *args, **kwargs):
        kwargs = kwargs or {}
        return json.dumps({
            "jsonrpc": "2.0",
            "method": 'call',
            "params": {
                "service": service,
                "method": method,
                "args": args
            },
            "id": random.randint(0, 1000000000),
        })
