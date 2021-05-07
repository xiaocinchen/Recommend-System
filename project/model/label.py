from flask import Flask, jsonify,request
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from .__init__ import db
from util.logger import logger


class Label(db.Model):
    __tablename__ = 'label'
    id = db.Column(db.INTEGER,primary_key = True)
    labelname = db.Column(db.String(30))
    count = db.Column(db.INTEGER)

    @classmethod
    def getLabelNum(self):
        sql = 'select count(*) from label'
        res = dict(list(db.engine.execute(sql).fetchall())[0])
        num = res['count(*)']
        logger.info(num)
        return num
    
    @classmethod
    def update(self,label):
        try:
            Lcount = Label.query.filter_by(labelname = label).first()
            Lcount.count += 1
            db.session.commit()
            logger.info(Lcount)
            return True
        except Exception as e:
            logger.error(e)
            return False
        
    @classmethod
    def getLabelNameFromId(self,id):
        sql = 'select labelname from label where id = '+str(id)
        res = dict(list(db.engine.execute(sql).fetchall())[0])['labelname']
        return res

    @classmethod
    def getSoloCount(self,id):
        sql = 'select count from label where id = '+str(id)
        res = dict(list(db.engine.execute(sql).fetchall())[0])['count']
        return int(res)

    @classmethod
    def getAllCount(self):
        sql = 'select sum(count) from label '
        res = dict(list(db.engine.execute(sql).fetchall())[0])['sum(count)']
        return int(res)
    
    @classmethod
    def getAllForSoloCount(self):
        sql = 'select * from label'
        res = list(db.engine.execute(sql).fetchall())
        ans = []
        ans.extend(dict(i) for i in res)
        return ans

        




            

        
