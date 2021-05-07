import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify,request

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