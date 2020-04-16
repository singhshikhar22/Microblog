# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 12:38:51 2020

@author: Shikhar Singh
"""

from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

