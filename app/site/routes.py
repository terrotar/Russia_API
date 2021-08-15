from flask import Blueprint, render_template, request
import requests

import haversine as hs
from haversine import Unit


site = Blueprint('site', __name__)


@site.route('/', methods=['GET'])
def index():
    return render_template('home_page.html')


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
