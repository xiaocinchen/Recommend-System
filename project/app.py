from flask import Flask,g,jsonify,request
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from model.__init__ import app
from lib.user import *
from lib.news import *

@app.route('/login/',methods=["POST"])
def login1():
    return login()

@app.route('/register/',methods=['POST'])
def register1():
    return register()

@app.route('/fenye/pagenum/<num>',methods=['GET'])
def fenye1(num):
    return fenye(num)

@app.route('/page',methods = ['GET'])
def page1():
    g.name = request.args.get('name')
    page = request.args.get('pagenum') 
    return getpage(page)

@app.route('/more',methods = ['GET'])
def getmore1():
    name = request.args.get('name')
    textname = request.args.get('textname')
    logger.info(name)
    return getmore(name,textname)

@app.route('/filternews',methods = ['GET'])
def filternews1():
    kind = request.args.get('kind')
    g.name = request.args.get('name')
    return filternews(kind)

if __name__ == '__main__':
    app.run()

