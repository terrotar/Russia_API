from flask import abort, Blueprint, request
import requests

# Library to calculate distance between two coordinates
import haversine as hs
from haversine import Unit

# Library to generate log file
from loguru import logger


# instance of Blueprint api with a url_prefix
api = Blueprint('api', __name__, url_prefix='/api')


# Route that calculate the distance between MKAD and the
# address typed by the user. It must be coordinate(first lng
# then lat) and float.
@api.route("/distance/<float:lng>/<float:lat>", methods=["GET"])
def distance(lng, lat):
    if(request.method == 'GET'):
        if(lng and lat):
            # As said im README.md, the parameter used to calculated inside
            # MKAD was the distance between Moscow(center of the radius) and
            # MKAD(edge of radius), which is equal 12.9 kms or 8 miles.
            # So, it calculate the distance between Moscow and the address
            # gave by the user less 12.9 kms or 8 miles.
            moscow = (37.622513, 55.75322)
            address = (lng, lat)
            dist = round(hs.haversine(moscow, address), 1)
            if(dist <= 12.9):
                return abort(400, {'ValueError': 'Distance inside MKAD.'})
            else:
                dist = round(dist - 12.9, 1)
                miles = round(hs.haversine(
                    moscow, address, unit=Unit.MILES), 1) - 8
                json = {"Address": {"Coordinates": {"Longitude": f"{lng}",
                                                    "latitude": f"{lat}"}
                                    },
                        "Distances": {"Kilometers": f"{dist}",
                                      "Miles": f"{miles}"}}
                logger.success(f"{json}")
                return json
        else:
            abort(400, "The coordinates in URL are invalid.")


# Route to get data of a certain place. It can be a name(Moscow) or
# coordinates(37.622513 55.75322, 37.622513,55.75322).
@api.route("/getdata/<address>", methods=["GET"])
def getdata(address):
    if(request.method == 'GET'):
        data = requests.get(
            f"https://geocode-maps.yandex.ru/1.x/?apikey=085b7527-0c65-43e9-b0e7-86b52fb93ffe&geocode={address}&format=json&lang=en-US&results=1")
        # Here I selected the number of results founds when a search is done but has no results founds.
        # To achieve it, I made a navigation inside the JSON response of the API to found the parameter "found"
        # and raise and Exception 400 when it's equal to 0.
        points = data.json()["response"]["GeoObjectCollection"]["metaDataProperty"]["GeocoderResponseMetaData"]["found"]
        for point in points:
            if(point == "0" or point == 0):
                return abort(400, "The coordinates or name in URL are invalid.")
            else:
                logger.success({"Address": f"{address}"})
                return data.json()
