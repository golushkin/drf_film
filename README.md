# Table of content
1. [About project](#desc)
2. [Requirements](#reqr)
3. [Installation](#inst)
4. [Routes](#rout)
5. [Demo](#demo)

<a name="desc"></a>
## About project

Drf_film is an api that allow you:
- do smt

<a name="reqr"></a>
## Requirements

- python
- django 
- django rest framework
- pipenv

<a name="inst"></a>
## Installation

1. Clone repository
```
git clone https://github.com/golushkin/drf_film.git
```
2. Go to dir drf_film
```
cd drf_film
```
3. Install pipenv
```
pip install pipenv
```
4. Install dependencies
```
pipenv install
```
5. Run server
```
pipenv shell
py manage.py runserver
```

<a name="rout"></a>
## Routes

1. Route: api/v1/user/
  - Methods: 
    - POST - create new user and return it
  - Required filds: usernmae, password
  - Fields:
    - username - string, must be an unique,
    - password - string,
    - email - email

2. Route: api/v1/man/
  - Methods: 
    - GET - return all people,
    - POST - create new person and return it
  - Required filds: first_name, last_name
  - Fields:
    - first_name - string, max length 30 characters,
    - last_name - string, max length 30 characters,
    - date_of_born - date, format YYYY-MM-DD

3. Route: api/v1/man/<int:pk>
  - Methods: 
    - GET - retrieve person,
    - DELETE - delete person
  - Required filds: pk
  - Fields:
    - pk - int, primary key

<a name="demo"></a>
## Demo

[**Demo**](#)