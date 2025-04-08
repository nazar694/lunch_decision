import pytest


@pytest.mark.django_db
def test_login_success(api_client, user):
    response = api_client.post('/api/user/login/', {
        'username': 'Employee',
        'password': 'password'
    })
    assert response.status_code == 200
    assert 'access' in response.data
    assert 'refresh' in response.data


@pytest.mark.django_db
def test_login_failure_wrong_password(api_client, user):
    response = api_client.post('/api/user/login/', {
        'username': 'Employee',
        'password': 'wrongpassword'
    })
    assert response.status_code == 401
    assert 'access' not in response.data


