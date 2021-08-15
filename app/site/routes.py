from flask import Blueprint, render_template, request
import requests

import haversine as hs
from haversine import Unit


site = Blueprint('site', __name__)


@site.route('/', methods=['GET'])
def index():
    return render_template('home_page.html')


@site.route("/distance/<float:lng>/<float:lat>", methods=["GET", "POST"])
def distance(lng, lat):
    if(request.method == 'POST'):
        moscow = (37.622513, 55.75322)
        address = (lng, lat)
        dist = round(hs.haversine(moscow, address), 1)
        if(dist <= 12.9):
            return render_template('home_page.html',
                                   value_error=True)
        else:
            dist = round(dist - 12.9, 1)
            miles = round(hs.haversine(
                moscow, address, unit=Unit.MILES), 1) - 8
            return render_template('home_page.html',
                                   address=address,
                                   kilometers=dist,
                                   miles=miles)
