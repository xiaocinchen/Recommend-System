from flask import Flask, jsonify,request
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from .__init__ import db
from datetime import datetime
import pickle
from model.textwithlabel import TextWithLabel
from util.logger import logger
from util.math import getListSum

class UserWithLabel(db.Model):
    __tablename__ = 'userwithlabel'
    id = db.Column(db.INTEGER,primary_key=True)
    name = db.Column(db.String(30))
    labelmartix = db.Column(db.LargeBinary)   #用户打标签的计数

    @classmethod
    def update(self,name,textname):
        sql = 'select * from userwithlabel where name = \'%s\' '%(name)
        res = dict(list(db.engine.execute(sql).fetchall())[0])
        label = pickle.loads(res['labelmartix'])
        martix = TextWithLabel.getSoloLabelMartix(textname)
        for m in martix:
            logger.debug(label[m])
            label[m] += 1
            logger.warning(label[m])
        logger.info(getListSum(label))
        label = pickle.dumps(label)
        # sql = 'update userwithlabel set label = '
        try:
            UserWithLabel.query.filter_by(name = name).update({'labelmartix':label})
            db.session.commit()
            return True
        except Exception as e:
            logger.error(str(e.args))
            return False

    @classmethod
    def add(self,name,labelmartix):
        info = UserWithLabel(name = name,labelmartix = labelmartix)
        try:
            db.session.add(info)
            db.session.commit()
            return 1
        except Exception as e:
            logger.error(str(e))
            return 0

    @classmethod
    def read(self,name):
        sql = 'select * from userwithlabel where name = \'%s\' '%(name)
        res = dict(list(db.engine.execute(sql).fetchall())[0])
        label = pickle.loads(res['labelmartix'])
        logger.info(getListSum(label))
        return label

    @classmethod
    def readAll(self):  
        sql = 'select labelmartix from userwithlabel'
        res = list(db.engine.execute(sql).fetchall())
        ans = []
        ans.extend(dict(i) for i in res)    
        return ans
