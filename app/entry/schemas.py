from flask import request, jsonify

from flask_marshmallow import Marshmallow
from entry.models import Entry
from server import *

ma = Marshmallow(app)

class EntrySchema(ma.ModelSchema):
    class Meta(ma.ModelSchema.Meta):

        '''
        This is schema model that defines fields to be accepted as input from the user, where id is automatically generated and foreign key is competition_id
        '''
        model = Entry
        sqla_session = db.session
        id = fields.Number(dump_only=True)
        title = fields.String(required=True)
        topic = fields.String(required=True)                #required=True indicates mandatory field
        state = fields.String(required=True)
        country = fields.String(required=True)
        competition_id = fields.Number(required=True)