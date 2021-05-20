from lib import user
from flask import Flask, jsonify,request
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import pickle
from .__init__ import db
from datetime import datetime
from util.logger import logger

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer,primary_key=True)
    textname = db.Column(db.String(100))
    username = db.Column(db.String(30))
    content=db.Column(db.TEXT)

    @classmethod
    def queryContentFromName(self,textname):
        sql = 'select * from comment where textname = \'%s\''%(textname)
        res = list(db.engine.execute(sql).fetchall())
        return res 

    @classmethod
    def add(self,content,username,textname):
        try:
            comment = Comment(content=content,username=username,textname=textname)
            db.session.add(comment)
            db.session.commit() 
            return 1
        except Exception as e:
            logger.error(str(e.args))
            return 0

