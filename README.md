# django-conoha
ConoHaオブジェクトストレージとDjangoを連携するカスタムストレージ

## Install
```bash
pip install git+https://github.com/Compeito/django-conoha
```

## Usage
settings.pyに以下を追加
```python
INSTALLED_APPS = [
    'conoha'
]

DEFAULT_FILE_STORAGE = 'conoha.storage.backend.ConohaObjectStorage'

# ...

CONOHA_ACCESS_FILE_PATH = 'conoha.json'

# or 

CONOHA_TENANT_ID = 'hogehoge'
CONOHA_ACCESS_TOKEN_ID = 'fugafuga'
```

conoha.jsonは下記コマンドで取得も可能  
```bash
# api_username, api_password, tenant_idは置き換える
python manage.py token_request api_username api_password tenant_id > conoha.json
```
