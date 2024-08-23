from dotenv import load_dotenv
import os
import requests

# Загрузка переменных окружения
load_dotenv()
api_key = os.getenv("api_key")

def get_weather(api_key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_github_user(username):
    url = f'<https://api.github.com/users/{username}>'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None