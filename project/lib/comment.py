from logging import log
from lib import user
from flask import Flask,g, jsonify,request
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import pickle
from datetime import datetime
from util.logger import logger
from model.comment import Comment

def getComment(textname):
    res = Comment.queryContentFromName(textname)
    ans = []
    ans.extend(dict(r) for r in res)
    logger.info("ans"+str(ans))
    data = {
        "content" : ans
    }
    return data

def addComment(textname,username,content):
    ans = Comment.add(content=content,username=username,textname=textname)
    logger.warning(ans)
    data = {
        'flag':ans
    }
    return data
    