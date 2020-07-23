from flask import Blueprint, jsonify, request, current_app, make_response, abort
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
@bp_characters.route('/character/<character_id>', methods=['GET'])
def get_one(character_id):
    print(character_id)
    character = Character.query.filter(Character.id == character_id).one_or_none()

    if character is not None:
        result = character_schema.dump(character)
        return jsonify(result)
    else:
        abort(404, f'Character not found for ID: {character_id} not found')


# create character
@bp_characters.route('/character', methods=['POST'])
def add_character():
    fname = request.json['fname']
    lname = request.json['lname']

    new_character = Character(fname, lname)

    """
    create condition to add new character ex: characters can't have 
    the same lname, so check if the lname alredy exist in the databse
    """
    condition = True

    # check if character can be created 
    if condition:
        current_app.db.session.add(new_character)
        current_app.db.session.commit()

        return character_schema.jsonify(new_character), 201
    else:
        abort(409, f"couldn't be created, because X")


# update character by id
@bp_characters.route('/character/<character_id>', methods=['PUT'])
def update_one(character_id):
    fname = request.json['fname']
    lname = request.json['lname']

    character = Character.query.get(character_id)
    print('character query', character)

    if character is not None:
        character.fname = fname
        character.lname = lname

        current_app.db.session.commit()

        return character_schema.jsonify(character)
    else:
        abort(404, f"character with ID: {character_id} was not found")


# delete character by id
@bp_characters.route('/character/<character_id>', methods=['DELETE'])
def delete_one(character_id):
    character = Character.query.get(character_id)

    if character is not None:
        current_app.db.session.delete(character)
        current_app.db.session.commit()
    
        return character_schema.jsonify(character)
    else:
        abort(404, f"character with ID: {character_id} was not found")
