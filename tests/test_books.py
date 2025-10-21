import pytest
from django.urls import reverse

from store.models import Book, Author, Publisher


@pytest.mark.django_db
def test_get_books(api_client, book_object):
    response = api_client.get("/books/", format="json")
    assert response.status_code == 200
    assert len(response.data) == 1


@pytest.mark.django_db
def test_get_books_empty(api_client):
    response = api_client.get("/books/", format="json")
    assert response.status_code == 200
    assert len(response.data) == 0


@pytest.mark.django_db
def test_create_book(api_client_admin, book_json, author, publisher):
    response = api_client_admin.post('/books/', book_json, format="json")

    assert response.status_code == 201
    assert response.data['title'] == book_json['title']
    assert response.data['description'] == book_json['description']
    assert response.data['author'] == book_json['author']
    assert response.data['publisher'] == book_json['publisher']
    assert response.data['pages'] == book_json['pages']
    assert response.data['price'] == book_json['price']
    assert response.data['year'] == book_json['year']
    assert response.data['available'] == book_json['available']


@pytest.mark.django_db
def test_create_book_unauthorized(api_client, book_json, author, publisher):
    response = api_client.post('/books/', book_json, format="json")

    assert response.status_code == 401
    assert Book.objects.count() == 0


@pytest.mark.django_db
def test_create_book_no_permissions(api_client_user, book_json, author, publisher):
    response = api_client_user.post('/books/', book_json, format="json")

    assert response.status_code == 403
    assert Book.objects.count() == 0


@pytest.mark.django_db
def test_create_book_invalid_data(api_client_admin, book_json):
    book_json['price'] = -200
    response = api_client_admin.post('/books/', book_json, format="json")

    assert response.status_code == 400
    assert Book.objects.count() == 0


@pytest.mark.django_db
def test_get_book(api_client, book_object):
    response = api_client.get("/books/1", format="json")

    assert response.status_code == 200
    assert response.data['id'] == 1


@pytest.mark.django_db
def test_get_nonexisting_book(api_client):
    response = api_client.get("/books/1", format="json")
    assert response.status_code == 404


@pytest.mark.django_db
def test_patch_book(api_client_admin, book_object):
    response = api_client_admin.patch("/books/1",
                                      {
                                          "price": 500,
                                          "year": 2025,
                                          "available": False
                                      },
                                      format="json")

    assert response.status_code == 200
    assert response.data['id'] == 1
    assert response.data['price'] == 500
    assert response.data['year'] == 2025
    assert response.data['available'] == False

@pytest.mark.django_db
def test_patch_book_unauthorized(api_client, book_object):
    response = api_client.patch("/books/1",
                                      {
                                          "price": 500,
                                          "year": 2025,
                                          "available": False
                                      },
                                      format="json")

    assert response.status_code == 401
    assert Book.objects.get(pk=1).price == book_object.price
    assert Book.objects.get(pk=1).year == book_object.year
    assert Book.objects.get(pk=1).available == book_object.available

@pytest.mark.django_db
def test_patch_book_invalid_data(api_client_admin, book_object):
    response = api_client_admin.patch("/books/1",
                                      {
                                          "price": -500,
                                          "year": 2025,
                                          "available": False
                                      },
                                      format="json")

    assert response.status_code == 400
    assert Book.objects.get(pk=1).price == book_object.price
    assert Book.objects.get(pk=1).year == book_object.year
    assert Book.objects.get(pk=1).available == book_object.available

@pytest.mark.django_db
def test_delete_book(api_client_admin, book_object):
    response = api_client_admin.delete("/books/1")

    assert response.status_code == 204
    assert Book.objects.count() == 0

@pytest.mark.django_db
def test_delete_book_unauthorized(api_client, book_object):
    response = api_client.delete("/books/1")

    assert response.status_code == 401
    assert Book.objects.count() == 1

@pytest.mark.django_db
def test_delete_book_no_permission(api_client_user, book_object):
    response = api_client_user.delete("/books/1")

    assert response.status_code == 403
    assert Book.objects.count() == 1