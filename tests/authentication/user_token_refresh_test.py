import pytest

@pytest.mark.django_db
def test_success(client, user_request, user_tokens):
    expected_response = ['access']

    response = client.post(
        '/api/v1/user/token/refresh/',
        data={
           **user_request,
           "refresh":  user_tokens['refresh']
        },
        format='json'
    )

    assert response.status_code == 200
    assert set(response.json().keys()) == set(expected_response)

@pytest.mark.django_db
def test_with_invalid_token(client, user_required_validation):
    expected_response = {
        "detail": "Token is invalid or expired",
        "code": "token_not_valid"
    }

    response = client.post(
        '/api/v1/user/token/refresh/',
        data={
        "refresh":  "asdasd"
        },
        format='json'
    )

    assert response.status_code == 401
    assert response.json() == expected_response

@pytest.mark.django_db
def test_with_empty(client):
    expected_response =  {
        "refresh": [
            "This field is required."
        ]     
    }

    response = client.post(
        '/api/v1/user/token/refresh/',
        data={
        },
        format='json'
    )

    print('test_without_refresh', response.json(), expected_response)

    assert response.status_code == 400
    assert response.json() == expected_response


