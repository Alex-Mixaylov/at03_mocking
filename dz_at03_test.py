
from dz_at03 import get_random_cat_image


def test_get_random_cat_image_success(mocker):
    """
    Тест проверяет успешный запрос к TheCatAPI и возвращает правильный URL изображения кошки.
    """
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {
            "id": "8mb",
            "url": "https://cdn2.thecatapi.com/images/8mb.jpg",
            "width": 500,
            "height": 375
        }
    ]

    # Мокируем requests.get для возврата заранее заданного ответа
    mock_get = mocker.patch("requests.get", return_value=mock_response)

    # Проверяем, что функция возвращает правильный URL
    assert get_random_cat_image() == "https://cdn2.thecatapi.com/images/8mb.jpg"
    mock_get.assert_called_once()  # Проверяем, что запрос был выполнен один раз


def test_get_random_cat_image_failure(mocker):
    """
    Тест проверяет неуспешный запрос (например, статус код 404) и возвращает None.
    """
    mock_response = mocker.Mock()
    mock_response.status_code = 404

    # Мокируем requests.get для возврата 404 ошибки
    mock_get = mocker.patch("requests.get", return_value=mock_response)

    # Проверяем, что функция возвращает None при неуспешном запросе
    assert get_random_cat_image() is None
    mock_get.assert_called_once()  # Проверяем, что запрос был выполнен один раз
