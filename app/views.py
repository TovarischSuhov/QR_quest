#!/usr/bin/env python

import qrcode
from flask import render_template, flash, redirect
from app import app
from forms import AddPoint
from app import objects

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add_point', methods = ['GET', 'POST'])
def add_point():
    form = AddPoint()
    if form.validate_on_submit():
        flash('Add object "' + form.name.data + '" with description "' + form.description.data + '"')
        return redirect('/')
    return render_template("add_point.html", form=form)

@app.route('/points')
def list_points():
    ojb = objects.find()
    return render_template("points.html", objects=obj)
