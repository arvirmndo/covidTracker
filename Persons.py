from flask import Flask, render_template, flash, redirect, url_for, g, request, jsonify
from wtforms import Form, StringField, validators
from wtforms.fields.core import SelectField
from datetime import datetime
import dbmodule

# #AddPersonForm
# class AddPersonForm(Form):
#     fname = StringField('fname', [validators.Length(min=1, max=50)])
#     email = StringField('email', [validators.Length(min=1, max=50)])
#     address = StringField('address', [validators.Length(min=1, max=50)])
#     contactNo = StringField('contactNo', [validators.Length(min=1, max=80)])

# def addPerson():
#     if request.method == 'POST':
#         fname = request.form['email']
#         email = request.form['email']
#         address = "Mabalanoy"
#         # address = form.address.data
#         contactNo = request.form['contactNo']

#         dbmodule.addPerson(fname, email, address, contactNo)

#         flash('Thank you for your cooperation!', 'success')
#         return redirect(url_for('index'))
#     else:
#         return render_template('index.html',)