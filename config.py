# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 13:20:33 2020

@author: Shikhar Singh
"""

import os
basedir=os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('test.prof2203@gmail.com')
    MAIL_PASSWORD = os.environ.get('@Moneykicks22')
    ADMINS = ['test.prof2203@gmail.com']
    
    POSTS_PER_PAGE = 3