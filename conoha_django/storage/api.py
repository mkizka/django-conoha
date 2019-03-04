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
            raise Exception(f'{str(response.status_code)}: {response.text}')

    def get(self, name):
        return self._request('get', f'{self.endpoint}/{name}')

    def put(self, name, f=None):
        return self._request('put', f'{self.endpoint}/{name}', data=f)

    def delete(self, name):
        return self._request('delete', f'{self.endpoint}/{name}')

    def get_dir_info(self, name):
        """
        nameに対応するファイルが存在するコンテナの情報か、空白なら全コンテナを返す
        """
        if name == '':
            return self.get('')

        container, filename = get_container_and_filename(name)
        return self.get(container)

    def get_path_info(self, name):
        """
        nameに対応するファイルもしくはコンテナの情報を返す
        """
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
        return self.get_path_info(name) is not None

    def info(self, name, k):
        return self.get_path_info(name)[k]
