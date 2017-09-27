#!/usr/bin/env python

from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, FileField
from wtforms.validators import Required

class AddPoint(Form):
    name = TextField('name', validators = [Required()])
    description = TextAreaField('description', validators = [Required()])
    photo = FileField("photo")
