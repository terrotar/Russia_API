from flask import Blueprint, render_template, request
import requests

import haversine as hs
from haversine import Unit


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
        moscow = (37.622513, 55.75322)
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
@site.route("/getdata/city", methods=["POST"])
def getdata_city():
    if(request.method == 'POST'):
        address = request.form["city"]
        if(address):
            data = requests.get(
                f"https://geocode-maps.yandex.ru/1.x/?apikey=085b7527-0c65-43e9-b0e7-86b52fb93ffe&geocode={address}&format=json&lang=en-US&results=1")
        return data.json()

