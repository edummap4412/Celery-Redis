import json

import requests


class ProductSDK():

    def __init__(self, base_url, auth):
        self.base_url = base_url
        self.auth = auth

    def create(self, data):
        url = f'{self.base_url}/products'
        header = {
            'Content-Type': 'application-json',
            'header': self.auth
        }

        response = requests.post(url=url, json=data, header=header)
        response.raise_for_status()
        return response.json()
