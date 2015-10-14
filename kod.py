# -*- coding: utf8 -*-x
#authors: Emma, Sandra, Linnea
"""from bottle import *"""
from bottle import *
import re, sys, mysql.connector
import urllib2
import urllib
import json


"""STARTSIDAN"""
@route('/')
def startsida():
        """Kör startsidan"""
        return template("index")


@route('/')
def text():
        """TEXT TEXT TEXT"""
        return template("text")


@route('/')
def test():
        """TEST TEST  TEST"""
        return template("test")


@route('/')
def best():
        """BEST BEST BEST"""
        return template("best")




run(debug=True, reloader=True, host='localhost', port=8080)
