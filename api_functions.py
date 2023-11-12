from requests import Response, Request
import config
import requests
import test_data as data

def createOrder(body: dict) -> Response:
    return requests.post(
        config.URL_SERVICE + config.CREATE_ORDER_PATH,
        headers=config.headers,
        json=body
    )


def getOrderDataByTrackNum(trackNum: int) -> Response:
    return requests.get(
        config.URL_SERVICE + config.GET_ORDER_DATA_PATH,
        params={"t": trackNum}
    )
