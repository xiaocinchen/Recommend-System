from flask import Flask, jsonify,request
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from .__init__ import db
from util.logger import logger
import pickle
import random


class RelistModel(db.Model):
    __tablename__ = 'relist'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),unique = True)
    textmatrix = db.Column(db.LargeBinary)   #推荐矩阵


    def add(name,textmatrix):
        info = RelistModel(name = name,textmatrix = textmatrix)
        try:
            db.session.add(info)
            db.session.commit()
            return 1
        except Exception as e:
            logger.error(str(e))
            return 0

    def getMatrix(name):
        sql = 'select * from relist where name = \''+name+'\''
        try:
            res = dict(list(db.engine.execute(sql).fetchall())[0])
            return pickle.loads(res['textmatrix'])
        except Exception as e:
            logger.info(str(e.args))
            RelistModel.add(name,pickle.dumps([random.randint(1,50)*x for x in range(0,100)]))
            return RelistModel.getMatrix(name)

    def update(name,text):
        textmatrix = pickle.dumps(text)
        if RelistModel.query.filter_by(name = name):    
            RelistModel.query.filter_by(name = name).update({'textmatrix':textmatrix})
        else:
            RelistModel.add(name,text)
        db.session.commit()
