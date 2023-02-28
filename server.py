from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= "postgresql://postgres:vastavik@localhost/vasu_database"
db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run(debug=True)