import pytest
from django.utils import timezone


@pytest.mark.django_db
def test_create_menu_success(auth_client, restaurant):
    response = auth_client.post('/api/menus/', {
        'restaurant': restaurant.id,
        'day': timezone.now().weekday(),
        'menu': 'Test menu'
    })
    assert response.status_code == 201


@pytest.mark.django_db
def test_duplicate_menu_for_same_day(auth_client, restaurant):
    data = {
        'restaurant': restaurant.id,
        'day': timezone.now().weekday(),
        'menu': 'Test menu'
    }
    auth_client.post('/api/menus/', data)
    response = auth_client.post('/api/menus/', data)
    assert response.status_code == 400
    assert 'non_field_errors' in response.data


@pytest.mark.django_db
def test_get_today_menu(auth_client, menu):
    response = auth_client.get('/api/menus/today/')
    assert response.status_code == 200
    assert isinstance(response.data, list)
    assert menu.menu in response.content.decode()


@pytest.mark.django_db
def test_today_menu_requires_auth(api_client, menu):
    response = api_client.get('/api/menus/today/')
    assert response.status_code == 401
