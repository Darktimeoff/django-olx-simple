import pytest
from django.contrib.auth.hashers import make_password

@pytest.fixture
def user_expected_resp():
    return {
        "id": 13,
        "password": make_password("test"),
        "last_login": None,
        "is_superuser": False,
        "username": "test",
        "first_name": "",
        "last_name": "",
        "email": "",
        "is_staff": False,
        "is_active": False,
        "date_joined": "2023-04-18T08:41:59.650703Z",
        "sex": "m",
        "role": "member",
        "age": 0,
        "groups": [],
        "user_permissions": [],
        "locations": []
    }

@pytest.fixture
def user_request():
    return {
        "username": "test",
        "password": "test"
    }