from flask import Flask, jsonify,request
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import pickle
from lib.label import CountLabel
from datetime import datetime
from model.userwithlabel import UserWithLabel
from util.logger import logger
from util.math import getListSum

def init_userwithlabel(name):
    username = name
    hobby = [0]*CountLabel()
    hobbyblob = pickle.dumps(hobby)
    if UserWithLabel.add(username,hobbyblob) == 1:
        logger.info('Success to init labelmartix')
    else:
        logger.error('Fail to init labelmartix')

def getAllSum(*name): #获取打标签的计数和
    s = 0
    if (len(name) == 0):
        res = UserWithLabel.readAll()
        for r in res:
            s += getListSum(pickle.loads(r['labelmartix']))
    else:
        res = UserWithLabel.read(name[0])
        s = getListSum(res)
    return s
