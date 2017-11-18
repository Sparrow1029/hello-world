#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import render_template, flash, redirect, session, url_for,request,g
from flask_login import login_user, logout_user, current_user, login_required
from CRUDapp import app, db, lm, oid
from .forms import LoginForm
from .models import User


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Pooty'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in O-town!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'Thor - Ragnarok was so comedic.'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))