from flask import Blueprint, request
import requests


api = Blueprint('api', __name__, url_prefix='/api')


@api.route("/<address>", methods=["GET"])
def getdata(address):
    if(request.method == 'GET'):
        data = requests.get(
            f"https://geocode-maps.yandex.ru/1.x/?apikey=085b7527-0c65-43e9-b0e7-86b52fb93ffe&geocode={address}&format=json&lang=en-US&results=1")
        return data.json()
