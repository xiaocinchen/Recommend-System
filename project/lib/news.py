from flask import Flask, jsonify,request
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sys
sys.path.append("..")
from model.user import User
from model.news import *
from model.__init__ import app,db
from model.userwithlabel import UserWithLabel
from model.textwithlabel import TextWithLabel
from lib.hobby import recommend
from lib.label import updateLabel
from util.logger import logger

kinddic = {'体育':'sportsnews','财经':'finanews','教育':'edunews','股票':'sharesnews','彩票':'lotterynews','时政':'currentnews','房产':'housenews','家居':'homenews','科学':'sciencenews','游戏':'gamenews','娱乐':'enternews','时尚':'fashionnews','社会':'socialnews','星座':'starnews'}

def fenye(num):
    #news = db.session.query(Sportsnews.content,Sportsnews.title,Sportsnews.textname,Sportsnews.date,Sportsnews.author).filter(User.nickname==nickname,User.passwd==passwd).one()
    # cl = [conlist]*4
    data = {
        "list":[],
        "id":num,
        "totalPage":2,
        "pagesize":10,
        "total":7,
    }
    logger.info('aaaaaaaaaa')
    return jsonify(data)

def getpage(page):
    res = list(News.queryOnePage(offset = int(page)-1))
    count = list(News.queryCount())
    logger.info('total '+str(count[0][0]))
    newsdata = []
    newsdata.extend(dict(r) for r in res)
    data = {
        "list":newsdata,
        "total":count[0][0]
    }
    # logger.info('fufufufufufu')
    return jsonify(data)

def getmore(name,textname):
    res = list(News.queryMore(textname).fetchall())
    newsdata = []
    newsdata.extend(dict(r) for r in res)
    data = {
        "list":newsdata[0]
    }
    UserWithLabel.update(name,textname)
    label = TextWithLabel.getSoloLabelMartix(textname)
    updateLabel(label)
    # UserWithLabel.read(name)
    return jsonify(data)

def filternews(kind):
    kind = kind.split()
    g.flag = 1
    if len(kind) == 0:
        g.flag = 0
    for i,k in enumerate(kind):
        kind[i] = kinddic[k]
    # logger.debug(kind)
    res = list(News.queryOnePage(10,0,*kind)) if g.flag == 1 else list(News.queryOnePage())
    newsdata = []
    newsdata.extend(dict(r) for r in res)
    data = {
        "list":newsdata,
        "id":3,
        "totalPage":2,
        "pagesize":len(res),
        "total":7,
    }
    return jsonify(data)

    