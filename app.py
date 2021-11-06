from flask import Flask, render_template, flash, redirect, url_for, request, jsonify
from wtforms import Form, StringField, validators
from wtforms.fields.core import SelectField
from datetime import datetime
import dbmodule
import Persons

app = Flask(__name__)

@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        fname = request.form['fname']
        email = request.form['email']
        brgy = request.form['barangay']
        city = request.form['city']
        province = request.form['province']

        address = brgy + ", " + city + ", " + province
        # address = form.address.data
        contactNo = request.form['contactNo']

        dbmodule.addPerson(fname, email, address, contactNo)

        # flash('Thank you for your cooperation!', 'success')
        return redirect(url_for('index'))
    else:
        return render_template('index.html')

# @app.route('/addPerson', methods=['GET', 'POST'])
# def addPersonInfo():
#     addPerson = Persons.addPerson()
#     return addPerson

if __name__ == '__main__':
    app.run(debug=True)