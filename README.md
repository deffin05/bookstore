# Bookstore

It's a website for a bookstore. You can see list of books, sort and
filter them, add new books, publishers and authors. Also it has 
authorization and user profiles.


## Endpoints
**GET** `/books`
- Get list of books
- Response status: `200`
- Parameters:
  - book_name: book name we are searching for
  - author_name: author we are searching for
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
**GET** `/books/{id}`
- Get a specific book
- Response status: `200`
- Response body:
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

**PATCH** `/books/{id}`
- Update info of a book
- Response status: `204`
- Request body:
```json
{
    "price": 399,
    "available": false
}
```

**DELETE** `/books/{id}`
- Deletes a book
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
- Request body:
```json
{
    "name": "Joanne Rowling"
}
```
**GET** `/authors/{id}`
- Get books of a specific author
- Response status: `200`
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

**PATCH** `/autohrs/{id}`
- Update info of an author
- Response status: `204`
- Request body:
```json
{
    "name": "J. K. Rowling"
}
```

**DELETE** `/author/{id}`
- Deletes an author
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
- Request body:
```json
{
    "name": "Ababagalamaga"
}
```
**GET** `/publishers/{id}`
- Get books of a specific publisher
- Response status: `200`
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

**PATCH** `/publishers/{id}`
- Update info of a publisher
- Response status: `204`
- Request body:
```json
{
    "name": "Ablablababa"
}
```

**DELETE** `/publishers/{id}`
- Deletes a publisher
- Response status: `204`
---
**GET** `/account`
- Get account info
- Response status: `200`, `401`
- Response body:
```json
[
    "first_name": "Dmytro",
    "last_name": "Heh",
    "phone_number": "+3801414171",
    "email": "dmytro@gmail.com"
]
```

**POST** `/account`
- Create a new account
- Response status: `201`
- Request body:
```json
[
    "first_name": "Dmytro",
    "last_name": "Heh",
    "phone_number": "+380671417153",
    "email": "dmytro@gmail.com"
]
```
**PATCH** `/account/{id}`
- Update account info
- Response status: `204`, `401`
- Request body:
```json
{
    "first_name": "Anton",
    "phone_number": "+380975041668"
}
```

**DELETE** `/account/{id}`
- Deletes an account
- Response status: `204`, `401`
---
**GET** `/account/orders`
- Get orders of the user
- Response status: `200`, `401`
- Response body:
```json
[
    {
        "id": 1,
        "items": [
            {
                "id": 1,
                "title": "Harry Potter",
                "price": 300,
                "author": "Joanne Rowling"
            },
            ...
        ],
        "date": "12-05-2025",
        "price": 1000
    },
    ...
]
```

**POST** `/account/orders`
- Create a new order
- Response status: `201`, `401`
- Request body: (list of book id's)

```json
[
    1,2,3,4...
]
```
---
**GET** `/account/cart`
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

**POST** `/account/cart`
- Add a book to the cart
- Response status: `201`, `401`
- Request body:

```json
{
    "id": 1
}
```
**PATCH** `/account/cart/{id}`
- Update info of the book in the cart(quantity)
- Response status: `204`, `401`
- Response body:
```json
{
    "quantity": 5
}
```

**DELETE** `/account/cart/{id}`
- Remove a book from the cart
- Response status: `204`, `401`

## Database diagram
<img width="840" height="667" alt="database_diagram" src="https://github.com/user-attachments/assets/79f2e62a-453d-4106-9e2e-17a97215cb29" />