import json

import requests

from .utils import load_credentials, get_container_and_filename


class ObjectStorageApi:
    def __init__(self):
        self._credentials = load_credentials()
        self.token_id = self._credentials['access']['token']['id']
        self.tenant_id = self._credentials['access']['token']['tenant']['id']
        self.endpoint = f'https://object-storage.tyo1.conoha.io/v1/nc_{self.tenant_id}'

    def _request(self, method, url, **kwargs):
        headers = {
            'Accept': 'application/json',
            'X-Auth-Token': self.token_id
        }
        response = requests.request(method, url, headers=headers, **kwargs)
        try:
            return response.json()
        except:
            raise Exception

    def get(self, name):
        return self._request('get', f'{self.endpoint}/{name}')

    def create(self, name, f=None):
        return self._request('put', f'{self.endpoint}/{name}', data=f)

    def _get_container_or_file_info(self, name):
        container, filename = get_container_and_filename(name)

        if filename:
            data = self.get(container)
            target = filename
        else:
            data = self.get('')
            target = container

        for obj in data:
            if obj['name'] == target:
                return obj

    def exists(self, name):
        return self._get_container_or_file_info(name) is not None

    def info(self, name, k):
        return self._get_container_or_file_info(name)[k]
