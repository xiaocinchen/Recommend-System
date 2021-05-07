from flask import Flask,g, jsonify,request
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from model.label import Label
from model.__init__ import db
from util.logger import logger

def CountLabel():
    return Label.getLabelNum()

def updateLabel(label):
    logger.info(str(label))
    try:
        for l in label:
            logger.debug(l)
            Label.update(Label.getLabelNameFromId(int(l)))
    except Exception as e:
        logger.error(e)
