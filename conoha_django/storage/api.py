import json
from pathlib import Path

import requests
from django.core import files

from ..utils import load_credentials


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
        except json.decoder.JSONDecodeError:
            return response

    def _get_containers(self):
        return self._request('get', self.endpoint)

    def container(self, name):
        self._request('put', f'{self.endpoint}/{name}')
        return ObjectStorageContainer(name)


class ObjectStorageContainer(ObjectStorageApi):
    def __init__(self, name):
        super().__init__()
        self.endpoint += f'/{name}'

    def container(self, name):
        raise Exception

    def upload(self, filepath, filename=None):
        filename = Path(filepath).name if filename is None else filepath
        with open(filepath, 'rb') as f:
            self._request('put', f'{self.endpoint}/{filename}', data=f)


class ObjectStorageFile(files.File):
    pass
