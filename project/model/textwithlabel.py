from flask import Flask, jsonify,request
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from model.label import Label
from .__init__ import db
from util.logger import logger

class TextWithLabel(db.Model):
    __tablename__ = 'textwithlabel'
    textname = db.Column(db.String(30),primary_key = True)
    label = db.Column(db.String(200))  

    @classmethod
    def getLabelMartix(self):
        sql = 'select * from textwithlabel'
        res = list(db.engine.execute(sql).fetchall())
        ans = []
        ans.extend(dict(i) for i in res)
        return ans

    @classmethod
    def getSoloLabelMartix(self,textname):
        sql = 'select * from textwithlabel where textname = \'%s\''%(textname)
        res = dict(list(db.engine.execute(sql).fetchall())[0])
        return list(eval(res['label']))


