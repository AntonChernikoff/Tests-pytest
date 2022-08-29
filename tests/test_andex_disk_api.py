import pytest
import requests
from pprint import pprint

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN = ''
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
path = "test_folder"

def test_create_folder():
    responce = requests.put(f'{URL}?path={path}', headers=headers)
    pprint(responce)
    if responce.status_code == 201:
        print(f"Каталог path={path} создан")
    else:
        assert False, f"Ошибка создание каталога path={path}! Код ответа = {responce.status_code}"

def test_get_info():
    responce = requests.get(f'{URL}?path={path}', headers=headers)
    pprint(responce)
    if responce.status_code == 200:
        print(f"Каталог path={path} существует")
    else:
        assert False, f"Ошибка обращения к каталогу path={path}! Код ответа = {responce.status_code}"

def test_delete_catalog():
    path = 'test_folder'
    responce = requests.delete(f'{URL}?path={path}', headers=headers)
    pprint(responce)
    if responce.status_code == 204:
        print(f"Удаление каталога path={path} выполнено")
    else:
        assert False, f"Ошибка удаления каталога! Код ответа = {responce.status_code}"

