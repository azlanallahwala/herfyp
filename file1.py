# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 21:36:56 2018

@author: umer
"""
from flask import Flask
import os
from urllib import parse
import psycopg2
from psycopg2 import sql
import re, math
from textblob import TextBlob
from collections import Counter
import operator


app = Flask(__name__)


@app.route('/')
def use():
    try:
        print("sucessfull")
    except:
        print("failed")
    return 'Hello World12!'


if __name__ == '__main__':
    app.run()
