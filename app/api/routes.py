from flask import Blueprint, request
import requests

import haversine as hs
from haversine import Unit


# instance of Blueprint api
api = Blueprint('api', __name__, url_prefix='/api')


# Route that calculate the distance between MKAD and the
# address typed by the user. It must be coordinate(first lng
# then lat) and float.
@api.route("/distance/<float:lng>/<float:lat>", methods=["GET"])
def distance(lng, lat):
    if(request.method == 'GET'):
        moscow = (37.622513, 55.75322)
        address = (lng, lat)
        dist = round(hs.haversine(moscow, address), 1)
        if(dist <= 12.9):
            return {'ValueError': 'Distance inside MKAD.'}
        else:
            dist = round(dist - 12.9, 1)
            miles = round(hs.haversine(
                moscow, address, unit=Unit.MILES), 1) - 8
            return {'distance': {
                'Kilometers': dist,
                'Miles': miles}
            }


# Route to get data of a certain place. It can be a name(Moscow) or
# coordinates(37.622513 55.75322, 37.622513,55.75322).
@api.route("/getdata/<address>", methods=["GET"])
def getdata(address):
    if(request.method == 'GET'):
        data = requests.get(
            f"https://geocode-maps.yandex.ru/1.x/?apikey=085b7527-0c65-43e9-b0e7-86b52fb93ffe&geocode={address}&format=json&lang=en-US&results=1")
        return data.json()
