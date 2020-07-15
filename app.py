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
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

# product schema
class CharacterSchema(ma.Schema):
    class Meta:
        fields = ('id', 'fname', 'lname')


# init schema
character_schema = CharacterSchema()
characters_schema = CharacterSchema(many = True)

# get all characters
@app.route('/character', methods=['GET'])
def get_all():
    all_characters = Character.query.all()
    result = characters_schema.dump(all_characters)
    return jsonify(result)


# get character by id
@app.route('/character/<id>', methods=['GET'])
def get_one(id):
    # character = Character.query.filter(Character.id == id).one_or_none()
    character = Character.query.get(id)

    result = character_schema.dump(character)
    return jsonify(result)


# create character
@app.route('/character', methods=['POST'])
def add_character():
    fname = request.json['fname']
    lname = request.json['lname']

    new_character = Character(fname, lname)
    db.session.add(new_character)
    db.session.commit()

    return character_schema.jsonify(new_character)


# update character by id
@app.route('/character/<id>', methods=['PUT'])
def update_one(id):
    character = Character.query.get(id)

    fname = request.json['fname']
    lname = request.json['lname']

    character.fname = fname
    character.lname = lname

    db.session.commit()

    return character_schema.jsonify(character)


# delete character by id
@app.route('/character/<id>', methods=['DELETE'])
def delete_one(id):
    character = Character.query.get(id)

    db.session.delete(character)
    db.session.commit()

    return character_schema.jsonify(character)


# run server
if __name__ == '__main__':
    app.run(debug=True)