from flask_sqlalchemy import SQLAlchemy
import json
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin
import bcrypt

from settings import app

db = SQLAlchemy(app)

# Define models
users_roles = db.Table('appuser_role',
        db.Column('appuser_id', db.Integer(), db.ForeignKey('appuser.id')),
        db.Column('approle_id', db.Integer(), db.ForeignKey('approle.id')))

class Role(db.Model, RoleMixin):
    __tablename__ = 'approle'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    __tablename__ = 'appuser'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password_hash = db.Column(db.String(128))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=users_roles,
                            backref=db.backref('appuser', lazy='dynamic'))

    @property
    def password(self):
        raise AttributeError('password not readable')
    
    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)