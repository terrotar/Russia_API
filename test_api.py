import pytest
import requests

from app.api.routes import api


# Tests of route /api/getdata/<address>
def test_getdata_string():
    response = requests.get("http://127.0.0.1:5000/api/getdata/moscow")
    assert response.status_code == 200


def test_getdata_empty_string():
    blank = ""
    response = requests.get(f"http://127.0.0.1:5000/api/getdata/{blank}")
    assert response.status_code == 404


def test_getdata_whitespace_string():
    blank = " "
    response = requests.get(f"http://127.0.0.1:5000/api/getdata/{blank}")
    assert response.status_code == 400


def test_getdata_coordinate_string():
    coordinate = 56
    response = requests.get(f"http://127.0.0.1:5000/api/getdata/{coordinate}")
    assert response.status_code == 400


# Tests of route /api/distance/lng/lat
def test_distance_coordinate_integer():
    coordinate = 56
    response = requests.get(f"http://127.0.0.1:5000/api/disntace/{coordinate}/{coordinate}")
    assert response.status_code == 400
