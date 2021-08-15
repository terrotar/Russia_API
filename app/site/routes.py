from flask import Blueprint, render_template, request
import requests

site = Blueprint('site', __name__)


@site.route('/', methods=['GET'])
def index():
    return render_template('home_page.html')
