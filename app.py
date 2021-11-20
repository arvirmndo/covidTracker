from flask import Flask, render_template, flash, redirect, url_for, request, jsonify
from wtforms import Form, StringField, validators
from wtforms.fields.core import SelectField
from datetime import datetime, timedelta
import dbmodule

app = Flask(__name__)


@app.route('/stepOne', methods=['GET','POST'])
def stepOne():
    # results = dbmodule.getTemp()
    # temperature = results[0]
    if request.method == 'POST':
        h_temp = request.form['h_temp']
        
        return redirect(url_for('stepTwo',  h_temp =  h_temp))
    else:
        return render_template('temps.html')

@app.route('/stepTwo', methods=['GET', 'POST'])
def stepTwo():
    if request.method == 'POST':
        temp = request.args.get('h_temp')
        fname = request.form['fname']
        email = request.form['email']
        brgy = request.form['barangay']
        city = request.form['city']
        province = request.form['province']
        symptom = request.form['symptoms']
        messaged = 'no'
        address = brgy + ", " + city + ", " + province
        # address = form.address.data
        contactNo = request.form['contactNo']

        dbmodule.addPerson(temp, fname, email, address, contactNo,symptom, messaged)
        
        # flash('Thank you for your cooperation!', 'success')
        
        return redirect(url_for('thankyou'))
    else:
        return render_template('index.html')

@app.route('/')
def startPage():
    return render_template('startpage.html')

@app.route("/ajaxlivesearch",methods=["POST","GET"])
def ajaxlivesearch():
    
    if request.method == 'POST':
        cnx = dbmodule.db()
        cursor = cnx.cursor()

        query = ('SELECT temperature FROM gettemp')
        
        cursor.execute(query)
        results = cursor.fetchall()

        temperature = results[0]
        
    return jsonify({'htmlresponse': render_template('response.html', temperature = temperature)})

@app.route("/thankyou")
def thankyou():
    return render_template('thankyou.html')

# @app.route("/test")
# def test():
#     now = datetime.now()
#     now_minus = now - timedelta(hours = 1)
#     now_plus = now + timedelta(hours = 1)
#     email = dbmodule.getEmails(now_plus.hour, now_minus.hour, now.hour)
#     msg = Message('Hello from the other side!', sender = 'test@mail.io')
#     msg.recipients = ['recipient']

#     print(type(msg.recipients))
#     return render_template('test.html', len = len(email) ,email = email)

# @app.route('/addPerson', methods=['GET', 'POST'])
# def addPersonInfo():
#     addPerson = Persons.addPerson()
#     return addPerson

if __name__ == '__main__':
    app.secret_key = "abc" 
    app.run(host='192.168.1.35', port=5000, debug=True, threaded=False)