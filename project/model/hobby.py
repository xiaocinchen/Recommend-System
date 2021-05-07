from flask import Flask, jsonify,request
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import pickle
from .__init__ import db
from datetime import datetime
from util.logger import logger
import random

class Hobby(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),unique = True)
    hobbymartix = db.Column(db.LargeBinary)   #兴趣矩阵

    def add(name,hobbymartix):
        info = Hobby(name = name,hobbymartix = hobbymartix)
        try:
            db.session.add(info)
            db.session.commit()
            return 1
        except Exception as e:
            logger.error(str(e))
            return 0

    def getMartix(name):
        sql = 'select * from hobby where name = \''+name+'\''
        res = dict(list(db.engine.execute(sql).fetchall())[0])
        # logger.info(pickle.loads(res['hobbymartix']))
        return pickle.loads(res['hobbymartix'])


