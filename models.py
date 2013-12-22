from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sassberto:bigkneez@ppsdata.c3btmdaoc32l.us-east-1.rds.amazonaws.com:3306/PPSdata'
db = SQLAlchemy(app)

class DRG(db.Model):
    __tablename__ = u'DRG'

    DRG_Id = Column(Integer, primary_key=True)
    DRG_Definition = Column(String(255))
    DRG_Modifier = Column(String(255))

class Provider(db.Model):
    __tablename__ = u'Provider'

    Provider_Id = Column(Integer, primary_key=True)
    Provider_Name = Column(String(255))
    Provider_Street_Address = Column(String(255))
    Provider_City = Column(String(255))
    Provider_State = Column(String(25))
    Provider_Zip_Code = Column(Integer)

    #Relationship one-to-many to Procedures
    Procedures = relationship("Procedure")

    #relationship one-to-many Procedure
class Procedure(db.Model):
    __tablename__ = u'Procedure'

    id = Column(db.Integer, primary_key=True)
    DRG_Id = Column(Integer, ForeignKey(DRG.DRG_Id))
    #relationship to one-to-one Provider
    Provider_Id = Column(Integer, ForeignKey(Provider.Provider_Id))
    Total_Discharges = Column(Integer)
    Average_Covered_Charges = Column(String(25))
    Average_Total_Payments = Column(String(25))

    #relationship to one-to-one DRG
    DRG = db.relationship('DRG',backref=db.backref('DRG', lazy='dynamic'))
    Provider = db.relationship('Provider',backref=db.backref('Provider', lazy='dynamic'))

class PpsDataTable(db.Model):
    __tablename__ = u'PPSdata'

    id = Column(Integer, primary_key=True)
    DRG_Definition = Column(String(500))
    Provider_Id = Column(Integer)
    Provider_Name = Column(String(255))
    Provider_Street_Address = Column(String(255))
    Provider_City = Column(String(255))
    Provider_State = Column(String(25))
    Provider_Zip_Code = Column(Integer)
    Hospital_Referral = Column(String(255))
    Total_Discharges = Column(Integer)
    Average_Covered_Charges = Column(String(25))
    Average_Total_Payments = Column(String(25))