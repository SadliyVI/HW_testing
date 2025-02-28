import configparser
import pytest
import requests

config = configparser.ConfigParser()
config.read(r'settings.ini')
BASE_URL = 'https://cloud-api.yandex.net/v1/disk/resources'
YADI_TOKEN = config['Tokens']['yadi_token']
HEADERS = {'Authorization': f'OAuth {YADI_TOKEN}', 'Content-Type':
           'application/json'} if YADI_TOKEN else {}

@pytest.fixture(scope='module')
def create_folder_name():
    return 'test_folder'

@pytest.fixture(autouse=True)
def cleanup_folder(create_folder_name):
    yield
    requests.delete(f'{BASE_URL}?path={create_folder_name}', headers = HEADERS)

# Проверка успешного создания папки
def test_create_folder_success(create_folder_name):
    response = requests.put(f'{BASE_URL}?path={create_folder_name}',
                            headers = HEADERS)
    assert response.status_code in [200, 201], 'Папка не создана'

# Проверка на повторное создание папки
def test_folder_already_exist(create_folder_name):
    response = requests.put(f'{BASE_URL}?path={create_folder_name}',
                            headers = HEADERS)
    response = requests.put(f'{BASE_URL}?path={create_folder_name}',
                            headers = HEADERS)
    assert response.status_code == 409, 'Папка уже существует'


@pytest.mark.parametrize('headers_, path_, expected_code',  [
    (HEADERS,'my_files', 404),  # Не удалось найти запрошенный ресурс
    ({'Authorization': 'OAuth invalid_token'},'test_folder', 401) # Не авторизован
    ], ids=['no_resource', 'invalid_token'])
def test_create_folder_unauthorized(headers_,path_, expected_code):
    response = requests.patch(f'{BASE_URL}?path={path_}', headers=headers_)
    assert response.status_code == expected_code



