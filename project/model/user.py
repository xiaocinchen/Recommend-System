from flask import Flask, jsonify,request
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from .__init__ import db
from model.hobby import Hobby

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.INTEGER,primary_key=True)
    name = db.Column(db.String(20),unique=True)
    passwd = db.Column(db.String(50))
    email = db.Column(db.String(50))
    nickname = db.Column(db.String(30))
    
    def queryUser(username,passwd):
        # user = db.session.query(User.name,User.email,User.id).filter(User.nickname==nickname,User.passwd==passwd).one()
        sql = 'select * from user where name = \'%s\' and passwd = \'%s\''%(username,passwd)
        res = dict(list(db.engine.execute(sql).fetchall())[0])
        # Hobby.getMartix(res['name'])
        return res

    def addUser(userinfo):
        sql = 'insert into user (name,passwd,email,nickname) values ( \'%s\', \'%s\',\'%s\',\'%s\')'%(userinfo['name'],userinfo['passwd'],userinfo['email'],userinfo['nickname'])
        try:
            db.engine.execute(sql)
            return True
        except Exception as e:
            logger.error(str(e.args))
            return False
        