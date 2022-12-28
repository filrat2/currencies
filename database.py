# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# database config
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nbp.db'
db_nbp = SQLAlchemy(app)


# define database tables as classes
class Currency(db_nbp.Model):
    id = db_nbp.Column(db_nbp.Integer, primary_key=True)
    name = db_nbp.Column(db_nbp.String(50), unique=True,
                         nullable=False)
    code = db_nbp.Column(db_nbp.String(3), unique=True,
                         nullable=False)


class CurrencyDayMidRate(db_nbp.Model):
    __table_args__ = (db_nbp.UniqueConstraint('currency_id', 'date'),)
    id = db_nbp.Column(db_nbp.Integer, primary_key=True)
    currency_id = db_nbp.Column(db_nbp.Integer, db_nbp.ForeignKey('currency.id'))
    mid_rate = db_nbp.Column(db_nbp.Float, unique=False,
                             nullable=False)
    date = db_nbp.Column(db_nbp.Date, unique=False,
                         nullable=False)


# create database
with app.app_context():
    db_nbp.create_all()
