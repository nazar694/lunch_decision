import pytest
from django.utils import timezone

from django.contrib.auth.models import User
from rest_framework.test import APIClient
from restaurants.models import Restaurant, Menu


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(db):
    return User.objects.create_user(username='Employee', password='password')


@pytest.fixture
def auth_client(api_client, user):
    login = api_client.post('/api/user/login/', {
        'username': 'Employee',
        'password': 'password'
    })
    token = login.data['access']
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    return api_client


@pytest.fixture
def restaurant(db):
    return Restaurant.objects.create(name="Test restaurant")


@pytest.fixture
def menu(restaurant, db):
    return Menu.objects.create(
        restaurant=restaurant,
        day=timezone.now().weekday(),
        menu='Salad'
    )