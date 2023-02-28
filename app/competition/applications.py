from flask import Flask, request, jsonify, make_response
from server import app, db
from flask import request, jsonify

from competition.models import Competition
from competition.schemas import CompetitionSchema

from pickle import load, dump


@app.route('/v1/competition', methods = ['GET'])
def allthecompetitions():
    
    '''
    Define a function to fetch all the competitions
    '''
    get_competitions = Competition.query.all()                  # use .all() for all the competitions
    competition_schema = CompetitionSchema(many=True)
    competitions = competition_schema.dump(get_competitions)
    return make_response(jsonify({"Here are the competitions": competitions}))          #return the response in JSON format



@app.route('/v1/competition/<int:id>', methods=['GET'])
def competition_by_id(id):

    '''
    This function is used to fetch a particular competition based on id
    '''
    get_competition = Competition.query.get(id)                   #Get a single competition
    competition_schema = CompetitionSchema()
    one_competition = competition_schema.dump(get_competition)

    return make_response(jsonify(one_competition))         #display the output in JSON format



@app.route('/v1/competition/create', methods = ['POST'])
def create_competition():

    '''
    A function to create a user using fields specified in CompetitionSchema
    '''
    data = request.get_json()                 #get all the data in JSON format and store it in a variable
    competition_schema = CompetitionSchema()        #take the data from user schema
    competition = competition_schema.load(data)
    result = competition_schema.dump(competition.create())

    return make_response(jsonify({"Created": result}),200)


@app.route('/v1/competition/update/<id>', methods = ['PUT'])
def update_competition_by_id(id):

    '''
    This functions is defined to make changes in existing fields
    '''
    data = request.get_json()
    get_competition = Competition.query.get(id)         #fetch competition by id on which the operation is to be performed
    if data.get('name'):
        get_competition.name = data['name']             #update the entered name with the new name
    if data.get('status'):
        get_competition.status = data['status']         #update the entered status with the new status
    if data.get('description'):
        get_competition.description = data['description']   #update the entered description with the new one
    if data.get('user_id'):
        get_competition.user_id = data['user_id']           #update the entered user_id with the new user_id
    
    db.session.add(get_competition)
    db.session.commit()
    competition_schema = CompetitionSchema(only=['id', 'name', 'status','description', 'user_id'])
    competition = competition_schema.dump(get_competition)
    return make_response(jsonify({"Updated": competition}))         #display the message



@app.route('/v1/competition/delete/<id>', methods = ['DELETE'])
def delete_competition_by_id(id):

    '''
    A competition can be removed with the help of this function
    '''
    get_competition = Competition.query.get(id)
    db.session.delete(get_competition)                      #use .delete() to remove a competition with particular id
    db.session.commit()                                     #commit the changes
    return make_response("Deleted",204)