from django.core.files.storage import Storage

from pathlib import Path
from .api import ObjectStorageApi


class ConohaObjectStorage(Storage):

    def __init__(self):
        self.api = ObjectStorageApi()

    def _open(self):
        pass

    def _save(self):
        pass

    def path(self, name):
        return super().path(name)

    def delete(self, name):
        pass

    def exists(self, name):
        return not self.api.exists(name)

    def listdir(self, path):
        data = self.api.get(path)
        files = []
        dirs = []
        for obj in data:
            if 'content_type' in obj.keys():
                if not obj['content_type'] == 'application/directory':
                    files.append(obj['name'])
                    continue
            dirs.append(obj['name'])
        return dirs, files

    def size(self, name):
        return self.api.info(name, 'bytes')

    def url(self, name):
        return self.api.endpoint + name

    def get_valid_name(self, name):
        if name == '.':
            return ''

    def get_modified_time(self, name):
        return self.api.info(name, 'last_modified')
