import pytest


@pytest.mark.django_db
def test_successful_vote(auth_client, restaurant):
    response = auth_client.post('/api/votes/', {'restaurant': restaurant.id})
    assert response.status_code == 201


@pytest.mark.django_db
def test_vote_requires_auth(api_client, restaurant):
    response = api_client.post('/api/votes/', {'restaurant': restaurant.id})
    assert response.status_code == 401


@pytest.mark.django_db
def test_double_vote_not_allowed(auth_client, restaurant):
    auth_client.post('/api/votes/', {'restaurant': restaurant.id})
    response = auth_client.post('/api/votes/', {'restaurant': restaurant.id})
    assert response.status_code == 400
    assert 'non_field_errors' in response.data


@pytest.mark.django_db
def test_vote_with_token(api_client, user, restaurant):
    login = api_client.post('/api/user/login/', {
        'username': 'Employee',
        'password': 'password'
    })
    token = login.data['access']
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    response = api_client.post('/api/votes/', {'restaurant': restaurant.id})
    assert response.status_code == 201


@pytest.mark.django_db
def test_vote_results(auth_client, restaurant):
    auth_client.post('/api/votes/', {'restaurant': restaurant.id})
    response = auth_client.get('/api/votes/today/')
    assert response.status_code == 200
    assert response.data[0]['restaurant__name'] == restaurant.name
