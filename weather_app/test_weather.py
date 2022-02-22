import pytest
import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from weather import City, app


# test for app.py
@pytest.mark.parametrize(
    "test_input, expected",
    [
        (3 + 5, 8),
        (2 + 4, 6),
        (6 * 9, 54),
    ],
)
def test_eval_add(test_input, expected):
    assert test_input == expected


def test_city_name():
    city = City(name="New York")
    assert city.name == "New York"


def test_index_route_get():
    response = app.test_client().get("/")
    assert response.status_code == 200


def test_index_route_post():
    response = app.test_client().post("/", data={"city": "New York"})
    assert response.status_code == 200
    assert b"New York" in response.data
