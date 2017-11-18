#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'CRUDapp.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
# Setting this to suppress FSADeprecationWarning
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/08/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'https://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'https://www.google.com/accounts/08/id'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]