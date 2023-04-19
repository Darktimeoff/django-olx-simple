import pytest

@pytest.mark.django_db
def test_create_user(client, user_expected_resp, user_request):
    response = client.post(
        '/api/v1/user/',
       user_request,
       format='json'
    )
    user_expected_resp['id'] = response.json().get('id', None)
    user_expected_resp['date_joined'] = response.json().get('date_joined', None)
    user_expected_resp['password'] = response.json().get('password', None)
    
    assert response.status_code == 201
    assert response.json() == user_expected_resp

    