from flask import jsonify
import json
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin

from settings import app
from appuser.UserModel import *


@app.before_first_request
def create_user():
    try:
        db.create_all()
        user_datastore.create_user(email='Admin', password='password')
        db.session.commit()
    except:
        db.session.rollback()
        print("User created already...")

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login')
def get_student():
    pass

if __name__ == '__main__':
    app.run(port=5000)
