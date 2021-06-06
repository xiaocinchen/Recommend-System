from flask import Flask,g, jsonify,request
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from .__init__ import db
from datetime import datetime
from util.logger import logger
from util.math import getListSum
from lib.hobby import recommend
import random


class News(db.Model):
    __abstract__ = True
    __tablename__ = 'News'
    textname = db.Column(db.String(100), primary_key=True)
    content = db.Column(db.Text, unique=False)
    title = db.Column(db.Text)
    author = db.Column(db.String(50))

    @classmethod
    def randOnePage(self,*kind):
        logger.warning(kind)
        randlist = []
        if len(kind) > 0:
            sql = 'select textname,label from news where label = '
            for realkind in kind:
                for index,k in enumerate(realkind):
                    sql += '\''+ str(k) + '\' or label = ' if index != len(realkind)-1 else '\''+str(k) + '\' order by rand() limit 10'
        else:
            sql = 'select textname,label from news where (id = '
            for i in range(0,10):
                sql += str(random.randint(1,14000)) + ' or id = ' if i != 9 else str(random.randint(1,14000)) + ')'
        logger.info(sql)
        res = list(db.engine.execute(sql).fetchall())
        ans = []
        ans.extend(dict(i) for i in res)
        sql = ''
        for i,a in enumerate(ans):
            sql += 'select title,author,date,textname from %s where textname = \'%s\' union '%(a['label'],a['textname']) if i != len(ans)-1 else 'select title,author,date,textname from %s where textname = \'%s\''%(a['label'],a['textname']) 
        logger.info(sql)
        res = db.engine.execute(sql) 
        return res

    @classmethod
    def queryOnePage(self, num = 10,offset = 0,*kind):
        martix = recommend(g.name)
        relist = []
        if len(kind) > 0:
            logger.error(str(kind))
            if len(kind[0]) > 1:
                sql = 'select textname,label from news where ( label = '
                for index,k in enumerate(kind):
                    sql += '\''+ str(k) + '\' or label = ' if index != len(kind)-1 else '\''+str(k) + '\' )'
            else:
                sql = 'select textname,label from news where label = '
                for index,k in enumerate(kind):
                    sql += '\''+ str(k) + '\' or label = ' if index != len(kind)-1 else '\''+str(k) + '\' '
        else:
            sql = 'select textname,label from news '
        for i, m in enumerate(martix[int(offset)*int(num)+random.randint(10,50):]):
            if len(relist) > num:
                break
            realsql = sql + ' and id = '+str(m) if len(kind) != 0 else sql + 'where id = '+str(m)
            res = list(db.engine.execute(realsql).fetchall())
            logger.critical('rrrr'+str(res))
            if len(res) > 0:
                relist.append(dict(res[0]))
        logger.warning(res)
        logger.info(relist)
        sql = ''
        for i,a in enumerate(relist):
            sql += 'select title,author,date,textname from %s where textname = \'%s\' union '%(a['label'],a['textname']) if i != len(relist)-1 else 'select title,author,date,textname from %s where textname = \'%s\''%(a['label'],a['textname']) 
        logger.debug("sql :"+sql)
        if sql:
            # sql += ' limit %s,%s  '%(offset,num)
            res = db.engine.execute(sql)
        return res

    @classmethod
    def queryCount(self):
        sql = 'select count(*) from news'
        res = db.engine.execute(sql)
        return res

    @classmethod
    def queryMore(self,textname):
        sql = 'select label from news where textname = \'%s\' '%(textname)
        res = dict(list(db.engine.execute(sql).fetchall())[0])
        label = res['label']
        sql = 'select content,title from %s where textname = \'%s\' '%(label,textname)
        res = db.engine.execute(sql)
        return res
    
class LabelNews(News):
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


class ReNewslist(db.Model):
    __tablename__ = 'relist'
    textname = db.Column(db.String(30),primary_key=True)
    label = db.Column(db.String(30))
    priority = db.Column(db.Integer)
    

    
