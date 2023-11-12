# Тамара Гудкова 10-я когорта. Финальный проект. Инженер по тестированию +

import datetime
import test_data as data
import api_functions as apiFunctions
from requests import Response, Request

def getTomorrowDate() -> datetime:
    currentDate = datetime.date.today()
    # currentDate = datetime.datetime.now().isoformat()
    td_object = datetime.timedelta(days=1)
    # print('Next date', currentDate + td_object)
    return currentDate + td_object


def getDateStr(isoString: str) -> str:
    date = datetime.datetime.strptime(isoString, '%Y-%m-%dT00:00:00.000Z')
    year: int = date.year
    month: int  = date.month
    day: int  = date.day
    return str(year) + '-' + str(month) + '-' + str(day)


def getOrderTrackNum(
    orderData: dict[str, str | list[str] | int]
) -> int:
    requestBody: dict[str, str | list[str] | int] = orderData
    requestBody['deliveryDate'] = str(getTomorrowDate())
    # requestBody['deliveryDate'] = '2023-11-19'
    response: Response = apiFunctions.createOrder(requestBody)
    return response.json()['track']


def getOrderDataByTrackSuccessResponse(
    orderData: dict[str, str | list[str] | int]
):
    # Получить номер созданного заказа
    num: int = getOrderTrackNum(orderData)
    # Получить данные созданного заказа
    getOrderDataResponse = apiFunctions.getOrderDataByTrackNum(num)

    assert getOrderDataResponse.status_code == 200, 'Status code is ' + getOrderDataResponse.status_code
    assert getOrderDataResponse.reason == 'OK', 'Status text is ' + getOrderDataResponse.reason

    respJson = getOrderDataResponse.json()['order']
    assert respJson['firstName'] == orderData['firstName'],  respJson['firstName'] + ' does not match ' + orderData['firstName']
    assert respJson['lastName'] == orderData['lastName'],  respJson['lastName'] + ' does not match ' + orderData['lastName']
    assert  respJson['metroStation'] == orderData['metroStation'],  respJson['metroStation'] + ' does not match ' + orderData['metroStation']
    assert respJson['phone'] == orderData['phone'],  respJson['phone'] + ' does not match ' + orderData['phone']
    assert respJson['rentTime'] == orderData['rentTime'],  respJson['rentTime'] + ' does not match ' + orderData['rentTime']

    respJsonDate: str = getDateStr(respJson['deliveryDate'])
    assert respJsonDate == str(getTomorrowDate()),  respJsonDate + ' does not match ' + orderData['deliveryDate']
    assert respJson['comment'] == orderData['comment'],  respJson['comment'] + ' does not match ' + orderData['comment']
    assert respJson['phone'] == orderData['phone'],  respJson['phone'] + ' does not match ' + orderData['phone']
    assert respJson['color'] == orderData['color'],  respJson['color'] + ' does not match ' + orderData['color']


def testGetOrderDataByTrackValidData():
    getOrderDataByTrackSuccessResponse(data.orderData)