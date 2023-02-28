from flask import Flask, request, jsonify
from datetime import datetime
from sqlalchemy import Column , Integer , String  , DateTime , Boolean , Date
from app.competition.models import Competition
from server import *

class Entry(db.Model):
    
    '''
    This function creates a model in database with all the defined fields
    '''
    __tablename__ = "entry table"
    id = db.Column(db.Integer, primary_key=True)              #This is the primary key that increases automatically by one everytime is used
    title = db.Column(db.String(20))
    topic = db.Column(db.String(25))
    state = db.Column(db.String(25))
    country = db.Column(db.String(20))
    is_delete = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    competition_id = db.Column(db.Integer, db.ForeignKey(Competition.id))          #foreign key represents relationship between two models


    def create(self):

      '''
      This function adds the model and commits the changes in the database
      '''
      db.session.add(self)
      db.session.commit()
      return self
    
    def __init__(self,title,topic,state,country,competition_id):
        
        '''
        This function takes five arguments and assigns them to the corrosponding variables
        '''
        self.title = title
        self.topic = topic
        self.state = state
        self.country = country
        self.competition_id = competition_id

    def __repr__(self):                       #Constructor to return id
        return '' % self.id
db.create_all()