import pytest
from main import get_weather, get_github_user
from dotenv import load_dotenv
import os

def test_get_weather_success(mocker):
    mock_get = mocker.patch('main.requests.get') #изменение поведения функции get_weather
    mock_get.return_value.status_code = 200 # Создаем мок-ответ для успешного запроса
    mock_get.return_value.json.return_value = {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 273.15}
    }
    load_dotenv() # Загрузка переменных окружения
    api_key = os.getenv('api_key')
    city = 'London'
    weather_data = get_weather(api_key, city)
    assert weather_data == {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 273.15}
    }

def test_get_weather_with_error(mocker):
    mock_get = mocker.patch('main.requests.get') #изменение поведения функции get_weather
    mock_get.return_value.status_code = 404 # Создаем неправильный мок-ответ для иммитации недоступности сервиса погоды

    load_dotenv() # Загрузка переменных окружения
    api_key = os.getenv('api_key')
    city = 'London'
    weather_data = get_weather(api_key, city)
    assert weather_data == None

def test_get_github_user(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'login': 'nizavr',
        'id': 345178,
        'name': 'Nina'
    }
    user_data = get_github_user('nizavr')
    assert user_data == {
        'login': 'nizavr',
        'id': 345178,
        'name': 'Nina'
    }

def test_get_github_user_with_error(mocker):
   mock_get = mocker.patch('main.requests.get')
   mock_get.return_value.status_code = 500

   user_data = get_github_user('cat')
   assert user_data == None