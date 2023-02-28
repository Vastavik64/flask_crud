from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column , Integer , String  , DateTime , Boolean , Date
from app.user.models import User
from server import *

class Competition(db.Model):
    
    '''
    This function creates a model in database with all the defined fields
    '''
    __tablename__ = "competitions table"
    id = db.Column(db.Integer, primary_key=True)                #This is the primary key that increases automatically by one everytime is used
    name = db.Column(db.String(20))
    status = db.Column(db.String(30))
    is_active = db.Column(db.Boolean, default=True)
    is_delete = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.string(50))
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))         #foreign key represents relationship between two models


    def create(self):

      '''
      This function adds the model and commits the changes in the database
      '''
      db.session.add(self)
      db.session.commit()
      return self
    
    def __init__(self,name,status,description, user_id):
        
        '''
        This function takes four arguments and assigns them to the corrosponding variables
        '''
        self.name = name
        self.status = status
        self.desdescription =description
        self.user_id = user_id

    def __repr__(self):                           #Constructor to return id
        return '' % self.id
db.create_all()