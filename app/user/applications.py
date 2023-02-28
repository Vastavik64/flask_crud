from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from server import app, db
from flask import request, jsonify
from flask_marshmallow import Marshmallow
from user.models import User
from user.schemas import UserSchema
from pickle import load, dump


@app.route('/v1/user', methods = ['GET'])
def all_the_users():

    '''
    Define a function to fetch all the users
    '''
    get_users = User.query.all()                        # use .all() to get all the users
    user_schema = UserSchema(many=True)
    users = user_schema.dump(get_users)

    return make_response(jsonify({"Here are the users": users}))        #return the response in JSON format



@app.route('/v1/user/<int:id>', methods=['GET'])
def user_by_id(id):

    '''
    This function is used to fetch a particular user based on id
    '''
    get_user = User.query.get(id)                   #Get a single user
    user_schema = UserSchema()
    one_user = user_schema.dump(get_user)

    return make_response(jsonify(one_user))         #display the output in JSON format



@app.route('/v1/user/create', methods = ['POST'])
def create_user():

    '''
    A function to create a user using fields specified in UserSchema
    '''
    data = request.get_json()               #get all the data in JSON format and store it in a variable
    user_schema = UserSchema()                      #take the data from user schema
    user = user_schema.load(data)                   #deserializes JSON data into object
    display = user_schema.dump(user.create())        #serializes object into JSON

    return make_response(jsonify({"Created": display}),200)          #200 is a successful execution status code



@app.route('/v1/user/update/<int:id>', methods = ['PUT'])
def user_update(id):

    '''
    This functions is defined to make changes in existing fields
    '''
    data = request.get_json()
    get_user = User.query.get(id)               #fetch user by id on which the operation is to be performed

    if data.get('name'):
        get_user.name = data['name']            #update the entered name with the new name
    if data.get('birthdate'):
        get_user.birthdate = data['birthdate']     #update the entered birthdate with the new birthdate
    if data.get('gender'):
        get_user.gender = data['gender']          #update the entered gender with the new gender
    
    db.session.add(get_user)
    db.session.commit()
    user_schema = UserSchema(only=['id', 'name', 'birthdate','gender'])
    user = user_schema.dump(get_user)

    return make_response(jsonify({"Updated": user}))            #display the message



@app.route('/v1/user/delete/<id>', methods = ['DELETE'])
def user_delete(id):

    '''
    A user can be removed with the help of this function
    '''
    get_user = User.query.get(id)
    db.session.delete(get_user)                         #use .delete() to remove a user with particular id
    db.session.commit()                                 #commit the changes

    return make_response("Deleted",204)