import requests
from pprint import pprint

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN = ''
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
path = 'test_folder'

def create_folder(path):
    result = requests.put(f'{URL}?path={path}', headers=headers)
    return result

def test_create_folder():
    responce = create_folder("test_folder")
    pprint(responce)
    if responce.status_code == 201:
        print("Каталог создан")
    else:
        print(f"Ошибка создание каталога! = {responce.status_code}")

def test_get_info():
    responce = requests.get(f'{URL}?path={path}', headers=headers)
    pprint(responce)
    if responce.status_code == 200:
        print("Каталог существует")
    else:
        print(f"Ошибка обращения к каталогу! = {responce.status_code}")

def test_delete_catalog():
    responce = requests.delete(f'{URL}?path={path}', headers=headers)
    pprint(responce)
    if responce.status_code == 204:
        print("Удаление выполнено")
    else:
        print(f"Ошибка удаления каталога! = {responce.status_code}")

if __name__ == '__main__':
    test_create_folder()
    test_get_info()
    test_delete_catalog()
