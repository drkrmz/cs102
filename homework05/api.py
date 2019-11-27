import requests
import time

import config


def get(url, params={}, timeout=5, max_retries=5, backoff_factor=0.3):
    """ Выполнить GET-запрос
    :param url: адрес, на который необходимо выполнить запрос
    :param params: параметры запроса
    :param timeout: максимальное время ожидания ответа от сервера
    :param max_retries: максимальное число повторных запросов
    :param backoff_factor: коэффициент экспоненциального нарастания задержки
    """
    start_time = time.process_time()
    retry = 0
    delay = 0.1
    jitter = 0.1
    k = 0
    while retry <= max_retries and k == 0:
        try:
            response = requests.get(url, timeout=timeout)
        except requests.exceptions.ReadTimeout as ex:
            if retry == max_retries:
                print(ex)
                return None
        except requests.exceptions.HTTPError as ex:
            if retry == max_retries:
                print(ex)
                return None
        except requests.exceptions.ConnectionError as ex:
            if retry == max_retries:
                print(ex)
                return None
        else:
            k = 1
            return response
        retry += 1
        delay = delay * (backoff_factor + jitter)
        time.sleep(delay)


def get_friends(user_id, fields):
    """ Вернуть данных о друзьях пользователя
    :param user_id: идентификатор пользователя, список друзей которого нужно получить
    :param fields: список полей, которые нужно получить для каждого пользователя
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert isinstance(fields, str), "fields must be string"
    assert user_id > 0, "user_id must be positive integer"
    domain = config.VK_CONFIG['domain']
    access_token = config.VK_CONFIG['access_token']
    v = '5.103'
    query = f"{domain}/friends.get?access_token={access_token}&user_id={user_id}&fields={fields}&v={v}"
    response = get(query)
    return response.json()