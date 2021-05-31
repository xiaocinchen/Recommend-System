from flask import Flask,g,jsonify,request
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from model.__init__ import app
from lib.user import *
from lib.news import *
from lib.comment import *

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

@app.route('/comments',methods = ['GET'])
def getComment1():
    textname = request.args.get('textname')
    g.name = request.args.get('name')
    return getComment(textname)

@app.route('/comments',methods = ['POST'])
def addComment1():
    textname = request.form['textname']
    g.name = request.form['name']
    content = request.form['content']
    logger.warning(textname)
    return addComment(textname,g.name,content)

@app.route('/update',methods = ['PATCH'])
def updateInfo1():
    return updateInfo()

if __name__ == '__main__':
    app.run()


