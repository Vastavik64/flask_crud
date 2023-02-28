from flask import Flask, request, jsonify, make_response
from server import app, db
from flask import request, jsonify

from entry.models import Entry
from entry.schemas import EntrySchema
from pickle import load, dump


@app.route('/v1/entry', methods = ['GET'])
def alltheentries():

    '''
    Define a function to fetch all the entries
    '''
    get_entries = Entry.query.all()                             # use .all() for all the entries
    entry_schema = EntrySchema(many=True)
    entries = entry_schema.dump(get_entries)
    return make_response(jsonify({"Here are the entries": entries}))        #return the response in JSON format



@app.route('/v1/entry/<int:id>', methods=['GET'])
def entry_by_id(id):

    '''
    This function is used to fetch a particular entry based on id
    '''
    get_entry = Entry.query.get(id)                   #Get a single entry
    entry_schema = EntrySchema()
    one_entry = entry_schema.dump(get_entry)

    return make_response(jsonify(one_entry))         #display the output in JSON format



@app.route('/v1/entry/create', methods = ['POST'])
def create_entry():

    '''
    A function to create an entry using fields specified in EntrySchema
    '''
    data = request.get_json()               #get all the data in JSON format and store it in a variable
    entry_schema = EntrySchema()            #take the data from user schema
    entry = entry_schema.load(data)
    result = entry_schema.dump(entry.create())
    return make_response(jsonify({"Created": result}),200)          #200 is a successful execution status code


@app.route('/v1/entry/update/<id>', methods = ['PUT'])
def update_entry_by_id(id):

    '''
    This functions is defined to make changes in existing fields
    '''
    data = request.get_json()
    get_entry = Entry.query.get(id)                 #fetch entry by id on which the operation is to be performed
    if data.get('title'):
        get_entry.title = data['title']             #update the entered title with the new title
    if data.get('topic'):
        get_entry.topic = data['topic']             #update the entered topic with the new topic
    if data.get('state'):
        get_entry.state = data['state']             #update the entered state with the new state  
    if data.get('country'):
        get_entry.country = data['country']         #update the entered country with the new one
    if data.get('competition_id'):
        get_entry.competition_id = data['competition_id']   #update the entered competition_id with the new id
    
    db.session.add(get_entry)
    db.session.commit()
    entry_schema = EntrySchema(only=['id', 'title', 'topic','state','description', 'competition_id'])
    entry = entry_schema.dump(get_entry)
    return make_response(jsonify({"Updated": entry}))           #display the message



@app.route('/v1/entry/delete/<id>', methods = ['DELETE'])
def delete_entry_by_id(id):

    '''
    An entry can be removed with the help of this function
    '''
    get_entry = Entry.query.get(id)
    db.session.delete(get_entry)                        #use .delete() to remove an entry with particular id
    db.session.commit()                                 #commit the changes
    return make_response("Deleted",204)