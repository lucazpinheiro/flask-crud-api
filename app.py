from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# init app
app = Flask(__name__)

# define absolute path
basedir = os.path.abspath(os.path.dirname(__file__))

# dataase

# define path db
# db_uri = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
db_uri = 'sqlite:///' + os.path.join(basedir, 'lite.db')


# app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
# app.config['SQLACHLHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init db
db = SQLAlchemy(app)

# init ma
ma = Marshmallow(app)


# data model for Products

# data class/model
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(100), unique=True)
    # description = db.Column(db.String(200))
    # price = db.Column(db.Float)
    # qty = db.Column(db.Integer)
    fname = db.Column(db.String(100), unique=True)
    lname = db.Column(db.String(100), unique=True)

    # def __init__(self, name, description, price, qty):
    #     self.name = name
    #     self.description = description
    #     self.price = price
    #     self.qty = qty
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

# product schema
class CharacterSchema(ma.Schema):
    class Meta:
        # fields = ('id', 'name', 'description', 'price', 'qty')
        fields = ('id', 'fname', 'lname')


# init schema
character_schema = CharacterSchema(many = True)
# characters_schema = CharacterSchema(many = True, strict = True)

@app.route('/', methods=['GET'])
def get():
    return jsonify({ 'message': 'Hello world!' })

# run server
if __name__ == '__main__':
    app.run(debug=True)