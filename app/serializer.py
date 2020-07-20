from flask_marshmallow import Marshmallow
from .model import Character

# init ma
ma = Marshmallow()

def configure(app):
    ma.init_app(app)

# character schema
class CharacterSchema(ma.Schema):
    class Meta:
        # model = Character
        fields = ('id', 'fname', 'lname')
