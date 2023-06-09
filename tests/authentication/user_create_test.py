import pytest

@pytest.mark.django_db
def test_create_user(client, user_expected_resp, user_request):
    response = client.post(
        '/api/v1/user/',
       {
        "username": "test",
        "password": "test",
       },
       format='json'
    )
    user_expected_resp['id'] = response.json().get('id', None)
    user_expected_resp['date_joined'] = response.json().get('date_joined', None)
    user_expected_resp['password'] = response.json().get('password', None)
   
    assert response.status_code == 201
    assert response.json() == user_expected_resp

@pytest.mark.django_db
def test_without_password(client, user_request, user_required_validation):
    user_required_validation.pop('username') 

    expected_response = user_required_validation

    response = client.post(
        '/api/v1/user/',
        {
            'username': '1'
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
        '/api/v1/user/',
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
        '/api/v1/user/',
        {
        },
        format='json'
    )
    
    assert response.status_code == 400
    assert response.json() == user_required_validation