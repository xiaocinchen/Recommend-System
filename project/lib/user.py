from flask import Flask, jsonify,request
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sys
sys.path.append("..")
from model.user import User
from lib.userwithlabel import init_userwithlabel
from lib.hobby import init_hobby,recommend
from model.__init__ import app,db
from util.logger import logger

def login():
    username = request.form['uname']
    passwd = request.form['pwd']
    try:
        user = User.queryUser(username,passwd)
        user = {
            "nickname":user['nickname'],
            "name":user['name'],
            "email":user['email'],
            "flag":1,
            "id":user['id']
        }
        logger.info("flag")
        recommend(user['name'])
    except Exception as e: 
        logger.error(str(e.args))
        user = {
            "flag":3
        }
    return jsonify(user)

def register():
    username = request.form['uname']
    pwd = request.form['pwd']
    email = request.form['email']
    nickname = request.form["nicheng"]
    userinfo = {'name':username,'passwd':pwd,'email':email,'nickname':nickname}
    # userinfo = User(name = username,passwd = pwd,email = email,nickname = nickname)
    if (User.addUser(userinfo)):
        try:
            init_hobby(username)
            init_userwithlabel(username)
            data = {
                "flag":1
            }
        except Exception as e:
            logger.error('Error:'+str(e.args))
            data = {"flag":0}
    return data

    