
import requests


def get_random_cat_image():
    """
    Функция делает запрос к TheCatAPI для получения случайного изображения кошки.

    :return: URL изображения кошки, если запрос успешен, иначе None.
    """
    url = "https://api.thecatapi.com/v1/images/search"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data and 'url' in data[0]:
                return data[0]['url']
        return None
    except requests.RequestException:
        return None
