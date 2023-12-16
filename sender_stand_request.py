import configuration
import requests
import data


# Выполняем запрос на создание заказа
def create_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.NEW_ORDER_PATH,
                         json=data.order_body,
                         headers=data.headers)


# Получаем заказ по его номеру
def get_information_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.RECEIVE_ORDER_NUMBER + str(track),
                        headers=data.headers)
