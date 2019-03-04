import io

from django.core.files.storage import Storage

from .utils import get_container_and_filename, is_container
from .api import ObjectStorageApi


class ConohaObjectStorage(Storage):
    def __init__(self):
        self.api = ObjectStorageApi()

    def _open(self):
        pass

    def _save(self, name, content):
        self.api.put(name, content)

    def delete(self, name):
        self.api.delete(name)

    def exists(self, name):
        return self.api.exists(name)

    def listdir(self, path):
        """
        コンテナをディレクトリ、コンテナ以下は全てファイルとして扱う
        """
        data = self.api.get_dir_info(path)
        result = [obj['name'] for obj in data]
        if path == '':
            return result, []
        elif is_container(path):
            return [], result
        return [], []

    def size(self, name):
        return self.api.info(name, 'bytes')

    def url(self, name):
        return self.api.endpoint + name

    def get_modified_time(self, name):
        return self.api.info(name, 'last_modified')
