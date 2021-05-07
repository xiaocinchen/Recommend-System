from flask import Flask, jsonify, request
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
import functools
import re
import sys
import pickle
sys.path.append("..")



app = Flask(__name__)
CORS(app, resources=r'/*')

db = SQLAlchemy(app)

class Config(object):
    """配置参数"""
    # 设置连接数据库的URL
    user = 'root'
    password = 'spade521'
    database = 'nr'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://%s:%s@127.0.0.1:3306/%s' % (user, password, database)

    # 设置sqlalchemy自动更跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 查询时会显示原始SQL语句
    app.config['SQLALCHEMY_ECHO'] = True

    # 禁止自动提交数据处理
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False

app.config.from_object(Config)

class News(db.Model):
    __abstract__ = True
    textname = db.Column(db.String(100), primary_key=True)
    content = db.Column(db.Text)
    title = db.Column(db.Text)
    date = db.Column(db.DateTime)
    author = db.Column(db.String(50))

class LableNews(News):
    __tablename__ = 'news'
    label = db.Column(db.String(30))

class SportsNews(News):     #体育
    __tablename__ = 'sportsnews'

class EduNews(News):        #教育  
    __tablename__ = 'edunews'

class StarNews(News):       #星座
    __tablename__ = 'starnews'

class FinaNews(News):       #财经
    __tablename__ = 'finanews'

class LotteryNews(News):    #彩票
    __tablename__ = 'lotterynews'

class HomeNews(News):       #家居
    __tablename__ = 'homenews'

class FashionNews(News):    #时尚
    __tablename__ = 'fashionnews'

class ScienceNews(News):    #科技
    __tablename__ = 'sciencenews'

class SocialNews(News):     #社会
    __tablename__ = 'socialnews'

class CurrentNews(News):    #时政
    __tablename__ = 'currentnews'

class GameNews(News):       #游戏
    __tablename__ = 'gamenews'

class HouseNews(News):      #房产
    __tablename__ = 'housenews'

class EnterNews(News):      #娱乐
    __tablename__ = 'enternews'

class SharesNews(News):      #股票
    __tablename__ = 'sharesnews'

class Label(db.Model):
    __tablename__ = 'label'
    id = db.Column(db.Integer,primary_key=True)
    labelname = db.Column(db.String(30))

class Textwithlabel(db.Model):
    __tablename__ = 'textwithlabel'
    textname = db.Column(db.String(30),primary_key=True)
    label = db.Column(db.String(60))

def fliter(text):
    exp = re.compile("[^\S\r\n]")
    text = exp.sub('', text)
    return text
    # return ''.join(text.split(' '))

def cmp(x,y):
    if int(x[:-4])>int(y[:-4]):
        return 1
    else:
        return -1

filePath = "/Users/xiaoxinchen/Downloads/THUCNews/股票/"
filelist = []
for top, dirs, nondirs in os.walk(filePath):
    for i in nondirs:
        filelist.append(i)
filelist.sort(key=functools.cmp_to_key(cmp))
for i in range(0,1000):
    filename = filePath+filelist[i]
    with open(filename, 'r') as f:
        filetitle = f.readline()
        filetext = fliter(f.read())
    newsinfo = SharesNews(textname=filelist[i],content=filetext,title=filetitle)
    db.session.add(newsinfo)
    db.session.commit()
    newsinfo = LableNews(textname=filelist[i],label = 'sharesnews')
    db.session.add(newsinfo)
    db.session.commit()
# print(filelist[:100])

# with open('./recommend/Recommend-System/labelindex.txt','rb') as f:
#     k = pickle.load(f)
#     for key in k:
#         # labelname = key[key.rfind('/')+1:]
#         info = Label(id=int(k[key]),labelname = key)
#         db.session.add(info)
#         db.session.commit()

# with open('./recommend/Recommend-System/textlabelMartix.txt','rb') as f:
#     k = pickle.load(f)
#     for key in k:
#         textname = key[key.rfind('/')+1:]
#         info = Textwithlabel(textname = textname,label = str(k[key]))
#         db.session.add(info)
#         db.session.commit()
