## CRUD application built with Flask and SQLAlchemy

I decided to build this app to learn more about SQLAlchemy and how it works with Flask.

Right now the app is very simple, it has five endpoints for the character route:

```
GET /character
POST /character
GET /character/id
PUT /character/id
DELETE /character/id
```
The data structure for the character resource is the following:
```
{
    "fname": string,
    "lname": string
}
```

## Next changes

- The app uses an SQLite database, I'm planning on replacing it with a Postgres connection.
- Add a more complex data model.
- Add more routes with query possibilities.

## ```Hot to run```

First, you will need to have ```Python 3.8``` and ```Pipenv``` installed.

0. Clone the repo and navigate to the root of the project
0. Run ```Pipenv Shell```
0. Run ```python build_database.py``` this will create an ```SQLite``` database and will add some initial data
0. Finally, run ```python app.py```

Now you can make requests to ```http://localhost:5000/character```


## running app
```sh
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True

flask run
```
migration

```sh
flask db init
flask db migrate
flask db upgrade
```
