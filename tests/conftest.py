import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient

from store.models import Author, Publisher, Book


@pytest.fixture
def api_client():
    yield APIClient()


@pytest.fixture
def user():
    yield User.objects.create_user(
        username='user',
        password='123',
    )


@pytest.fixture
def admin_user():
    yield User.objects.create_superuser(
        username='user',
        password='123',
    )


@pytest.fixture
def api_client_user(api_client, user):
    yield login(api_client)

@pytest.fixture
def api_client_admin(api_client, admin_user):
    yield login(api_client)

def login(api_client):
    login_url = reverse('token_obtain_pair')
    tokens = api_client.post(
        login_url, {'username': 'user', 'password': '123'}, format="json"
    ).data

    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + tokens['access'])

    return api_client


@pytest.fixture
def author():
    yield Author.objects.create(name="bla")

@pytest.fixture
def publisher():
    yield Publisher.objects.create(name="bla")

@pytest.fixture
def book_json():
    yield {
        "title": "book",
        "description": "blabla",
        "author": 1,
        "publisher": 1,
        "pages": 1,
        "price": 300,
        "year": 2020,
        "available": True,
    }

@pytest.fixture
def book_object(book_json, author, publisher):
    book_json["author"] = author
    book_json["publisher"] = publisher

    yield Book.objects.create(**book_json)