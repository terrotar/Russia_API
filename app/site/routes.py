from flask import abort, Blueprint, render_template, request
import requests

# Library to calculate distance between two coordinates
import haversine as hs
from haversine import Unit


# instance of Blueprint site
site = Blueprint('site', __name__)


# Route of home page with instructions of how to consume the API
# and anothers functionalities.
@site.route('/', methods=['GET'])
def index():
    return render_template('home_page.html')


# Route to calculate the distance based on longitude and latitude
# inserted as input and submmited with buttons by the user in a more
# visual display as alternative of the route API.
@site.route("/distance", methods=["POST"])
def distance():
    if(request.method == 'POST'):
        lng = request.form["longitude"]
        lat = request.form["latitude"]
        # As said im README.md, the parameter used to calculated inside MKAD
        # was the distance between Moscow(center of the radius) and
        # MKAD(edge of radius), which is equal 12.9 kms or 8 miles.
        # So, it calculate the distance between Moscow and the address gave
        # by the user less 12.9 kms or 8 miles.
        moscow = (37.622513, 55.75322)
        if(lng == "" or lng == " " or lat == "" or lat == " "):
            return abort(400, "The coordinates or name in URL are invalid.")
        else:
            address = (float(lng), float(lat))
            dist = round(hs.haversine(moscow, address), 1)
            if(dist <= 12.9):
                return render_template('home_page.html',
                                       value_error=True)
            else:
                km = round(dist - 12.9, 1)
                miles = round(hs.haversine(
                    moscow, address, unit=Unit.MILES), 1) - 8
                return render_template('home_page.html',
                                       address=address,
                                       kilometers=km,
                                       miles=miles)


# Route to display data of an address based on longitude and latitude or
# city and street name inserted as input and submmited with buttons by the user
# in a more visual display as alternative of the route API. Does the same thing
# of the Blueprint API /api/getdata but a little more friendly to understand
# how does it work.

# Here it's important to notice that was divided the search address in 2 parts:
# One searching by the city or street name
# Another searching by the coordinates longitude and latitude

# Route that search by city or steet
@site.route("/getdata/city", methods=["POST"])
def getdata_city():
    if(request.method == 'POST'):
        address = request.form["city"]
        if(address):
            data = requests.get(
                f"https://geocode-maps.yandex.ru/1.x/?apikey=085b7527-0c65-43e9-b0e7-86b52fb93ffe&geocode={address}&format=json&lang=en-US&results=1")
            # Here I selected the number of results founds when a search is done but has no results founds.
            # To achieve it, I made a navigation inside the JSON response of the API to found the parameter "found"
            # and raise and Exception 400 when it's equal to 0.
            points = data.json()[
                "response"]["GeoObjectCollection"]["metaDataProperty"]["GeocoderResponseMetaData"]["found"]
            for point in points:
                if(point == "0" or point == 0):
                    return abort(400, "The coordinates or name in URL are invalid.")
                else:
                    return data.json()
        else:
            return abort(400, "The coordinates or name in URL are invalid.")


# Route that search by longitude and latitude
@site.route("/getdata/coordinate", methods=["POST"])
def getdata_coordinate():
    if(request.method == 'POST'):
        lng = request.form["longitude"]
        lat = request.form["latitude"]
        if(lng == "" or lng == " " or lat == "" or lat == " "):
            return abort(400, "The coordinates or name in URL are invalid.")
        else:
            address = (float(lng), float(lat))
            data = requests.get(
                f"https://geocode-maps.yandex.ru/1.x/?apikey=085b7527-0c65-43e9-b0e7-86b52fb93ffe&geocode={address}&format=json&lang=en-US&results=1")
            # Here I selected the number of results founds when a search is
            # done but has no results founds. To achieve it, I made a and
            # raise and Exception 400 when it's equal to 0.
            points = data.json()[
                "response"]["GeoObjectCollection"]["metaDataProperty"]["GeocoderResponseMetaData"]["found"]
            for point in points:
                if(point == "0" or point == 0):
                    return abort(400, "The coordinates or name in URL are invalid.")
                else:
                    return data.json()
