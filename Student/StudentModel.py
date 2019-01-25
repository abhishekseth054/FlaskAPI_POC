from flask import Flask
import sqlalchemy.dialects.mysql
from flask_sqlalchemy import SQLAlchemy
import json

from settings import app, mydb

db = SQLAlchemy(app)

class StudentModel(db.Model):
    __tablename__ = 'students'
    id= mydb.Column(mydb.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    isbn = db.Column(db.Integer)
    
def get_all_student(self):
        return [StudentModel.json(StudentModel) for StudentModel in StudentModel.query.all()]

