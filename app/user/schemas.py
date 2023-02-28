from flask import request, jsonify

from flask_marshmallow import Marshmallow

from user.models import User
from marshmallow import fields

from server import *

ma = Marshmallow(app)

class UserSchema(ma.ModelSchema):
    class Meta(ma.ModelSchema.Meta):
        
        '''
        This is schema model that defines fields to be accepted as input from the user, where id is automatically generated
        '''
        model = User
        sqla_session = db.session
        id = fields.Number(dump_only=True)
        name = fields.String(required=True)                     #required=True indicates mandatory field
        birthdate = fields.Date(required=True)
        gender = fields.String(required=True)