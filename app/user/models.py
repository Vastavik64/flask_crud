from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column , Integer , String  , DateTime , Boolean , Date

from server import *

class User(db.Model):
    
    '''
    This function creates a model in database with all the defined fields
    '''
    __tablename__ = "users table"
    id = db.Column(db.Integer, primary_key=True)            #This is the primary key that increases automatically by one everytime is used
    name = db.Column(db.String(20), unique=True, nullable=False)
    birthdate = db.Column(db.Date)
    gender = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    is_delete = db.Column(db.Boolean, default=False)


    def create(self):

      '''
      This function adds the model and commits the changes in the database
      '''
      db.session.add(self)
      db.session.commit()
      return self
    
    
    def __init__(self,name,birthdate,gender):
        
        '''
        This function takes three arguments and assigns them to the corrosponding variables
        '''
        self.name = name
        self.birthdate = birthdate
        self.gender = gender

    def __repr__(self):               #Constructor to return id
        return '' % self.id

db.create_all()