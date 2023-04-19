import pytest
from django.contrib.auth.hashers import make_password

@pytest.fixture
@pytest.mark.django_db
def user_expected_resp(user):
    return {
        "id": user.pk,
        "password": user.password,
        "last_login": None,
        "is_superuser": False,
        "username": "test",
        "first_name": "",
        "last_name": "",
        "email": "",
        "is_staff": False,
        "is_active": False,
        "date_joined": user.date_joined,
        "sex": "m",
        "role": "member",
        "age": 0,
        "groups": [],
        "user_permissions": [],
        "locations": []
    }

@pytest.fixture
@pytest.mark.django_db
def user_request(user):
    return {
        "username": user.username,
        "password": "test"
    }

@pytest.fixture
def user_required_validation():
    return {
        "username": [
            "This field is required."
        ],
        "password": [
            "This field is required."
        ]
    }

@pytest.fixture
@pytest.mark.django_db
def user_tokens(client, user_request):
    response = client.post(
        '/api/v1/user/token/',
        user_request,
        format='json'
    )

    return response.json()