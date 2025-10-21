# Bookstore

It's a website for a bookstore. You can see list of books, sort and
filter them, add new books, publishers and authors. Also it has 
authorization and user profiles.


## Endpoints
**GET** `/books`
- Get list of books
- Response status: `200`
- Parameters:
  - book: book name we are searching for
  - author: author we are searching for
  - sort: the way we are sorting the list
  - page
  - publisher: filter by a specific publisher
  - genre: filter by a specific genre
- Response body:
```json
[
    {
        "id": 1,
        "title": "Harry Potter",
        "price": 300,
        "author": "Joanne Rowling",
        "available": true
    },
    ...
]
```

**POST** `/books`
- Create a new book
- Response status: `201`
- Headers:
    - Authorization: "Bearer `JWT access token`"
- Request body:
```json
{
    "title": "Harry Potter",
    "description": "...",
    "price": 300,
    "author": "Joanne Rowling",
    "publisher": "Ababagalamaga",
    "pages": 345,
    "year": 2005,
    "available": true
}
```
- Response body:
```json
{
    "id": 1,
    "title": "Harry Potter",
    "description": "...",
    "price": 300,
    "author": "Joanne Rowling",
    "publisher": "Ababagalamaga",
    "pages": 345,
    "year": 2005,
    "available": true
}
```
**GET** `/books/{id}`
- Get a specific book
- Response status: `200`
- Response body:
```json
{
    "id": 1,
    "title": "Harry Potter",
    "description": "...",
    "price": 300,
    "author": "Joanne Rowling",
    "publisher": "Ababagalamaga",
    "pages": 345,
    "year": 2005,
    "available": true
}
```

**PATCH** `/books/{id}`
- Update info of a book
- Response status: `200`
- Headers:
    - Authorization: "Bearer `JWT access token`"
- Request body:
```json
{
    "price": 399,
    "available": false
}
```
- Response body:
```json
{
    "id": 1,
    "title": "Harry Potter",
    "description": "...",
    "price": 399,
    "author": "Joanne Rowling",
    "publisher": "Ababagalamaga",
    "pages": 345,
    "year": 2005,
    "available": false
}
```

**DELETE** `/books/{id}`
- Deletes a book
- Headers:
    - Authorization: "Bearer `JWT access token`"
- Response status: `204`
---
**GET** `/authors`
- Get list of authors
- Response status: `200`
- Response body:
```json
[
    {
        "id": 1,
        "name": "Joanne Rowling"
    },
    ...
]
```

**POST** `/authors`
- Create a new author
- Response status: `201`
- Headers:
    - Authorization: "Bearer `JWT access token`"
- Request body:
```json
{
    "name": "Joanne Rowling"
}
```
- Response body:
```json
{
    "id": 1,
    "name": "Joanne Rowling"
}
```
**GET** `/authors/{id}`
- Get a specific author
- Response status: `200`
- Response body:
```json
{
    "id": 1,
    "name": "Joanne Rowling"
}
```

**PATCH** `/autohrs/{id}`
- Update info of an author
- Response status: `200`
- Headers:
    - Authorization: "Bearer `JWT access token`"
- Request body:
```json
{
    "name": "J. K. Rowling"
}
```
- Response body:
```json
{
    "id": 1,
    "name": "J. K. Rowling"
}
```

**DELETE** `/author/{id}`
- Deletes an author
- Headers:
    - Authorization: "Bearer `JWT access token`"
- Response status: `204`
---
**GET** `/publishers`
- Get list of publisherss
- Response status: `200`
- Response body:
```json
[
    {
        "id": 1,
        "name": "Ababagalamaga"
    },
    ...
]
```

**POST** `/publishers`
- Create a new publisher
- Response status: `201`
- Headers:
    - Authorization: "Bearer `JWT access token`"
- Request body:
```json
{
    "name": "Ababagalamaga"
}
```
- Response body:
```json
{
    "id": 1,
    "name": "Ababagalamaga"
}
```
**GET** `/publishers/{id}`
- Get a specific publisher
- Response status: `200`
- Response body:
```json
{
    "id": 1,
    "name": "Ababagalamaga"
}
```

**PATCH** `/publishers/{id}`
- Update info of a publisher
- Response status: `200`
- Headers:
    - Authorization: "Bearer `JWT access token`"
- Request body:
```json
{
    "name": "Ablablababa"
}
```
- Response body:
```json
{
    "id": 1,
    "name": "Ablablababa"
}
```

**DELETE** `/publishers/{id}`
- Deletes a publisher
- Headers:
    - Authorization: "Bearer `JWT access token`"
- Response status: `204`
---
**GET** `/users/{user_id}`
- Get account info, if you are not admin and use not your id, it will instead use your
- Response status: `200`, `401`
- Headers:
    - Authorization: "Bearer `JWT access token`"
- Response body:
```json
{
    "id": 1,
    "first_name": "Dmytro",
    "last_name": "Heh",
    "username": "deffin",
    "email": "dmytro@gmail.com"
}
```

**POST** `/users/`
- Create a new account
- Response status: `201`
- Request body:
```json
{
    "first_name": "Dmytro",
    "last_name": "Heh",
    "username": "deffin",
    "email": "dmytro@gmail.com",
    "password": "123"
}
```
- Response body:
```json
{
    "id": 1,
    "first_name": "Dmytro",
    "last_name": "Heh",
    "username": "deffin",
    "email": "dmytro@gmail.com"
}
```
**PATCH** `/users/{user_id}`
- Update account info
- Response status: `200`, `401`
- Headers:
    - Authorization: "Bearer `JWT access token`"
- Request body:
```json
{
    "first_name": "Anton",
    "email": "aoaoaoao@cok.co"
}
```
- Response body:
```json
{
    "id": 1,
    "first_name": "Anton",
    "phone_number": "+380975041668"
}
```

**DELETE** `/users/{user_id}`
- Deletes an account
- Headers:
    - Authorization: "Bearer `JWT access token`"
- Response status: `204`, `401`
---
**GET** `/account/{account_id}/orders`
- Get orders of the user
- Response status: `200`, `401`
- Response body:
```json
[
    {
        "id": 1,
        "items": [1, 2, 51, 12],
        "date": "12-05-2025",
        "price": 1000
    },
    ...
]
```

**POST** `/account/{account_id}/orders`
- Create a new order
- Response status: `201`, `401`
- Request body: (list of book id's)

```json
[
    1,2,3,4
]
```
- Response body:
```json
{
    "id": 1,
    "items": [1, 2, 3, 4], 
    "date": "12-05-2025",
    "price": 1000
}
```
---
**GET** `/account/{account_id}/cart`
- Get books in the cart
- Response status: `200`, `401`
- Response body:
```json
[
    {
        "id": 1,
        "title": "Harry Potter",
        "price": 300,
        "author": "Joanne Rowling",
        "quantity": 5,
        "available": true
    },
    ...
]
```

**POST** `/account/{account_id}/cart`
- Add a book to the cart
- Response status: `201`, `401`
- Request body:
```json
{
    "id": 1
}
```
**PATCH** `/account/{account_id}/cart/{book_id}`
- Update info of the book in the cart(quantity)
- Response status: `204`, `401`
- Request body:
```json
{
    "quantity": 5
}
```

**DELETE** `/account/{account_id}/cart/{book_id}`
- Remove a book from the cart
- Response status: `204`, `401`
---

**POST** /api/token
- Get JWT tokens
- Response statuses: `200`, `401`
- Request body:
```json
{
  "username": "main",
  "password": "123"
}
```
- Response body:
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR...",
    "access": "eyJhbGciOiJIUzI1NiIsInR5..."
}
```
**POST** /api/token/verify
- Verify JWT tokens
- Response statuses: `200`, `401`
- Request body:
```json
{
  "token": "meyJhbGciOiJIUzI1NiIsInR5..."
}
```
- Response body:
```json
{}
```
**POST** /api/token/refresh
- Refresh JWT access token
- Response statuses: `200`, `401`
- Request body:
```json
{
  "refresh": "meyJhbGciOiJIUzI1NiIsInR5..."
}
```
- Response body:
```json
{
  "access": "meyJhbGciOiJIUzI1NiIsInR5..."
}
```
## Database diagram
<img width="840" height="667" alt="database_diagram" src="https://github.com/user-attachments/assets/6a263048-f9f7-41a0-b34b-3301078bb571" />


## Run tests
```bash
pytest
```