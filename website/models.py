'''
models
'''

from datetime import timezone
from flask_login import UserMixin
from sqlalchemy.sql import func

from . import db


class User(db.Model, UserMixin):
    '''
    model for the User Object. inheritance from db.Model and UserMixin (for login)
    '''
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    loans = db.relationship('Loan', backref='user', lazy=True)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.TEXT)
    author = db.Column(db.String(150), nullable=False)
    year_of_publication = db.Column(db.Date, nullable=False)
    number_of_copies = db.Column(db.Integer, nullable=False)
    loans = db.relationship('Loan', backref='book',lazy=True)


class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_loan = db.Column(db.DateTime, nullable=False)
    end_loan = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                          nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'),
                        nullable=False)
    

    