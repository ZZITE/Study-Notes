#! /usr/bin/env python
# -*- coding: utf-8 -*-

from wtforms_tornado import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email


class EmailForm(Form):
    email = StringField(validators=[DataRequired(), Email()])


class OrderForm(Form):
    email = StringField(validators=[DataRequired(), Email()])
    firstName = StringField(validators=[DataRequired()])
    lastName = StringField(validators=[DataRequired()])
    address = StringField(validators=[DataRequired()])
    state = StringField(validators=[DataRequired()])
    city = StringField(validators=[DataRequired()])
    country = StringField(validators=[DataRequired()])
    zipcode = StringField(validators=[DataRequired()])
    size = StringField(validators=[DataRequired()])
    quantity = StringField(validators=[DataRequired()])
    phone = StringField()

