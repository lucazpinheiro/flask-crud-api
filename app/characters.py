from flask import Blueprint, jsonify, request, current_app
from .model import Character
from .serializer import CharacterSchema

bp_characters = Blueprint('characters', __name__)

# init schema
character_schema = CharacterSchema()
characters_schema = CharacterSchema(many = True)

# get all characters
@bp_characters.route('/character', methods=['GET'])
def get_all():
    all_characters = Character.query.all()
    result = characters_schema.dump(all_characters)
    return jsonify(result)


# get character by id
@bp_characters.route('/character/<id>', methods=['GET'])
def get_one(id):
    print(id)
    character = Character.query.filter(Character.id == id).one_or_none()
    character = Character.query.get(id)

    result = character_schema.dump(character)
    return jsonify(result)


# create character
@bp_characters.route('/character', methods=['POST'])
def add_character():
    fname = request.json['fname']
    lname = request.json['lname']

    new_character = Character(fname, lname)
    # new_character = Character(request.json)

    current_app.db.session.add(new_character)
    current_app.db.session.commit()

    return character_schema.jsonify(new_character)
    # return { 'message': 'ta indo'}

# update character by id
@bp_characters.route('/character/<id>', methods=['PUT'])
def update_one(id):
    character = Character.query.get(id)

    fname = request.json['fname']
    lname = request.json['lname']

    character.fname = fname
    character.lname = lname

    current_app.db.session.commit()

    return character_schema.jsonify(character)


# delete character by id
@bp_characters.route('/character/<id>', methods=['DELETE'])
def delete_one(id):
    character = Character.query.get(id)

    current_app.db.session.delete(character)
    current_app.db.session.commit()

    return character_schema.jsonify(character)
