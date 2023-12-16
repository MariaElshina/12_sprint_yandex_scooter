# Мария Ельшина, 11 когорта - Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data


# Подтверждаем успешное получение заказа по номеру
def positive_assert():
    response_new_order = sender_stand_request.create_new_order(data.order_body)
    track = response_new_order.json()['track']
    return sender_stand_request.get_information_order(track).status_code


#  Проверяем, что статус код = 200
def test_get_order_from_track():
    assert positive_assert() == 200
