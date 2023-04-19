import pytest

@pytest.mark.django_db
def test_user_login(client, user_request):
    expected_response = ['access', 'refresh']

    response = client.post(
        '/api/v1/user/token/',
        data=user_request,
        format='json'
    )

    assert response.status_code == 200
    assert set(response.json().keys()) == set(expected_response)

@pytest.mark.django_db
def test_pytest_user_login_not_found(client):
    expected_response = {
        "detail": "No active account found with the given credentials"
    }

    response = client.post(
        '/api/v1/user/token/',
        data={
            'username': 'not_found',
            'password': 'not_found'
        },
        format='json'
    )

    assert response.status_code == 401
    assert response.json() == expected_response

@pytest.mark.django_db
def test_without_password(client, user_request, user_required_validation):
    user_required_validation.pop('username') 

    expected_response = user_required_validation

    response = client.post(
        '/api/v1/user/token/',
        {
            'username': user_request['username']
        },
        format='json'
    )
    assert response.status_code == 400
    assert response.json() == expected_response

@pytest.mark.django_db
def test_without_username(client, user_request, user_required_validation):
    user_required_validation.pop('password') 

    expected_response = user_required_validation
     
    response = client.post(
        '/api/v1/user/token/',
        {
            'password':  user_request['password']
        },
        format='json'
    )

    assert response.status_code == 400
    assert response.json() == expected_response

@pytest.mark.django_db
def test_empty_request(client, user_required_validation):
    response = client.post(
        '/api/v1/user/token/',
        {
        },
        format='json'
    )
    
    assert response.status_code == 400
    assert response.json() == user_required_validation