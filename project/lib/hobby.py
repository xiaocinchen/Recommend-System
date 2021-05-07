from model.__init__ import app, db
from lib.label import CountLabel
from lib.userwithlabel import getAllSum
from util.logger import logger
from util.math import getListSum
from model.textwithlabel import TextWithLabel
from model.hobby import Hobby
from model.user import User
from model.userwithlabel import UserWithLabel
from model.label import Label
import pickle
from flask import Flask,g, jsonify, request
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sys
import numpy as np
sys.path.append("..")


def init_hobby(username):
    username = username
    hobby = [0]*CountLabel()
    hobbyblob = pickle.dumps(hobby)
    if (Hobby.add(username, hobbyblob) == 1):
        logger.info('Success to init hobbymartix')
    else:
        logger.error('Fail to init hobbymartix')


def recommend(username):
    usermartix = Hobby.getMartix(username)
    textmartix = TextWithLabel.getLabelMartix()
    hobby = []
    for i, tmartix in enumerate(textmartix):
        martix = list(eval(tmartix['label']))
        a = 0
        for m in martix:
            a += usermartix[int(m)]
        hobby.append(a)
    TFIDFMartix = np.array(calTFIDF(username))
    labelMartix = TextWithLabel.getLabelMartix()
    lastMartix = []
    for label in labelMartix:
        s = 0
        for i in list(eval(label['label'])):
            s += TFIDFMartix[int(i)]
        lastMartix.append(s)
    indexOfLastMartix = np.argsort(-np.array(lastMartix))
    return indexOfLastMartix

# def toHobby(username):

def calTFIDF(username):
    # user_hobby_sum = userinfodic[username]['user_hobby_sum']
    user_hobby_sum = getAllSum(username)
    all_user_hobby_sum = getAllSum()
    user_hobby = UserWithLabel.read(username)
    labelnum = Label.getLabelNum()
    TFIDFMartix = [0]*labelnum
    TFMartix = []
    IDFMartix = []
    all_user_all_label = Label.getAllCount()
    all_user_solo_label = Label.getAllForSoloCount()
    # cal TF
    for i,label in enumerate(user_hobby):
        TFMartix.append(label/(user_hobby_sum+1))
    # cal IDF
    for i in range(0, labelnum):
        IDFMartix.append(np.log(all_user_all_label/(all_user_solo_label[i]['count']+1)))
    # cal TF*IDF
    for i in range(0, labelnum):
        TFIDFMartix[i] = TFMartix[i]*IDFMartix[i]
    # logger.info(str(TFIDFMartix))
    return TFIDFMartix