from flask import request, jsonify

from flask_marshmallow import Marshmallow
from competition.models import Competition
from server import *

ma = Marshmallow(app)

class CompetitionSchema(ma.ModelSchema):
    class Meta(ma.ModelSchema.Meta):

        '''
        This is schema model that defines fields to be accepted as input from the user, where id is automatically generated and foreign key is user_id
        '''
        model = Competition
        sqla_session = db.session
        id = fields.Number(dump_only=True)
        name = fields.String(required=True)                    #required=True indicates mandatory field 
        status = fields.String(required=True)
        description = fields.String(required=True)
        user_id = fields.Number(required=True)