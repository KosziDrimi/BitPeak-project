# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 11:01:14 2021

@author: klimi
"""


import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bitpeak.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


class Programy(db.Model):
   
    __tablename__ = 'programy'

    id_program = db.Column(db.Integer,primary_key=True)
    nazwa = db.Column(db.Text)
    osie = db.relationship('Osie', backref='programy', lazy='dynamic')
    dzialania = db.relationship('Dzialania', backref='programy', lazy='dynamic')
    
    def __init__(self, id_program, nazwa):
        self.id_program = id_program
        self.nazwa = nazwa

    def __repr__(self):
        return f""" Program_ID: {self.id_program}, Program_nazwa: {self.nazwa} """
  

class Osie(db.Model):
   
    __tablename__ = 'osie'

    id_program = db.Column(db.Integer, db.ForeignKey('programy.id_program'))
    id_os = db.Column(db.Integer,primary_key=True)
    nazwa = db.Column(db.Text)
    dzialania = db.relationship('Dzialania', backref='osie', lazy='dynamic')
    
    def __init__(self, id_program, id_os, nazwa):
        self.id_program = id_program
        self.id_os = id_os
        self.nazwa = nazwa


class Dzialania(db.Model):
   
    __tablename__ = 'dzialania'

    id_program = db.Column(db.Integer, db.ForeignKey('programy.id_program'))
    id_os = db.Column(db.Integer, db.ForeignKey('osie.id_os'))
    id_dzl = db.Column(db.Integer,primary_key=True)
    nazwa = db.Column(db.Text)
    element = db.relationship('FTDElementy', backref='dzialania', lazy='dynamic')
    
    def __init__(self, id_program, id_os, id_dzl, nazwa):
        self.id_program = id_program
        self.id_os = id_os
        self.id_dzl = id_dzl
        self.nazwa = nazwa
    
    def __repr__(self):
        return f""" Program_ID: {self.id_program}, Os_ID: {self.id_os}, 
                    Dzialanie_ID: {self.id_dzl} """
    

class FTD(db.Model):
    __tablename__ = 'ftd'
    
    id_ftd = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.Text)
    opis = db.Column(db.Text)
    elementy = db.relationship('FTDElementy', backref='ftd', lazy='dynamic')
    
    def __init__(self, nazwa, opis):
      
        self.nazwa = nazwa
        self.opis = opis
        
    
class FTDElementy(db.Model):
    __tablename__ = 'ftdelementy'
     
    id_ftd_element = db.Column(db.Integer, primary_key=True)
    id_ftd = db.Column(db.Integer, db.ForeignKey('ftd.id_ftd'))
    id_dzl = db.Column(db.Integer, db.ForeignKey('dzialania.id_dzl'))
    
    def __init__(self, id_ftd, id_dzl):
      
        self.id_ftd = id_ftd
        self.id_dzl = id_dzl
        
     
        
 