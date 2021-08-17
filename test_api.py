import pytest
import requests


# Tests of route /api/getdata/<address>


# Test of a success request and response of the route
def test_getdata_correct_string():
    response = requests.get("http://127.0.0.1:5000/api/getdata/moscow")
    assert response.status_code == 200


# If the address is empty, it returns Page Not Found(404)
def test_getdata_empty_string():
    blank = ""
    response = requests.get(f"http://127.0.0.1:5000/api/getdata/{blank}")
    assert response.status_code == 404


# A blank address shall return code 400 due to the code in that Blueprint
def test_getdata_whitespace_string():
    blank = " "
    response = requests.get(f"http://127.0.0.1:5000/api/getdata/{blank}")
    assert response.status_code == 400


# Tests of route /api/distance/lng/lat


# Test of a success request and response of the route
def test_distance_correct_coordinate():
    lng = 40.406635
    lat = 56.129057
    response = requests.get(f"http://127.0.0.1:5000/api/distance/{lng}/{lat}")
    assert response.status_code == 200


# Test of an integer latitude that shall return an
# Exception 404(Page Not Found)
def test_distance_coordinate_integer_latitude():
    lng = 40.406635
    lat = 56
    response = requests.get(
        f"http://127.0.0.1:5000/api/distance/{lng}/{lat}")
    assert response.status_code == 404


# Test of an integer longitude that shall return an
# Exception 404(Page Not Found)
def test_distance_coordinate_integer_longitude():
    lng = 40
    lat = 56.129057
    response = requests.get(
        f"http://127.0.0.1:5000/api/distance/{lng}/{lat}")
    assert response.status_code == 404


# Test of a string longitude that shall return an
# Exception 404(Page Not Found)
def test_distance_coordinate_string_longitude():
    lng = "longitude"
    lat = 56.129057
    response = requests.get(
        f"http://127.0.0.1:5000/api/distance/{lng}/{lat}")
    assert response.status_code == 404


# Test of a string latitude that shall return an
# Exception 404(Page Not Found)
def test_distance_coordinate_string_latitude():
    lng = 40.406635
    lat = "latitude"
    response = requests.get(
        f"http://127.0.0.1:5000/api/distance/{lng}/{lat}")
    assert response.status_code == 404


# Test of an empty latitude that shall return an
# Exception 404(Page Not Found)
def test_distance_coordinate_empty_string_latitude():
    lng = 40.406635
    lat = ""
    response = requests.get(
        f"http://127.0.0.1:5000/api/distance/{lng}/{lat}")
    assert response.status_code == 404


# Test of an empty longitude that shall return an
# Exception 404(Page Not Found)
def test_distance_coordinate_empty_string_longitude():
    lng = ""
    lat = 56.129057
    response = requests.get(
        f"http://127.0.0.1:5000/api/distance/{lng}/{lat}")
    assert response.status_code == 404


# Test of a whitespace string latitude that shall return an
# Exception 404(Page Not Found)
def test_distance_coordinate_whitespace_string_latitude():
    lng = 40.406635
    lat = " "
    response = requests.get(
        f"http://127.0.0.1:5000/api/distance/{lng}/{lat}")
    assert response.status_code == 404


# Test of a whitespace string longitude that shall return an
# Exception 404(Page Not Found)
def test_distance_coordinate_whitespace_string_longitude():
    lng = " "
    lat = 56.129057
    response = requests.get(
        f"http://127.0.0.1:5000/api/distance/{lng}/{lat}")
    assert response.status_code == 404


# Test of an coordinate that is inside MKAD that
# shall return an Exception 404(Page Not Found)
# coordinates of Moscow to test
def test_distance_coordinate_inside_MKAD():
    lng = 37.622513
    lat = 55.75322
    response = requests.get(
        f"http://127.0.0.1:5000/api/distance/{lng}/{lat}")
    assert response.status_code == 400
