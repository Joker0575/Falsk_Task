from flask import Flask,redirect
from flask import render_template
from flask import g
from flask import request
from flask import request, jsonify
from flask.ext.mongoengine import MongoEngine
from textblob import TextBlob
import time


app = Flask(__name__)


app.config['MONGODB_SETTINGS'] = {
    'db': 'gomeloft_db',
    'host': 'localhost',
    'port': 27017
}

db = MongoEngine(app)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User(email=email,password=password)
        user.save()
        return redirect("/application", code=302)
    return render_template('index.html')


@app.route('/application',methods=['GET', 'POST'])
def application():
    text = Data.objects
    if request.method == 'POST':
        subject = request.form['subject']
        text_data = request.form['text_area']
        now = time.strftime("%c")
        data = Data(subject=subject,text_data=text_data,date=str(now))
        data.save()
        return redirect("/submitted_data", code=302)
    return render_template('app.html', text=text)

@app.route('/submitted_data',methods=['GET', 'POST'])
def submitted_data():
    data = Data.objects
    if request.method == 'POST':
        subject = request.form['subject']
        text_data = request.form['text_area']
        now = time.strftime("%c")
        data = Data(subject=subject,text_data=text_data,date=str(now))
        data.save()
    return render_template('submitted.html' ,text=data)


@app.route('/logout',methods=['GET'])
def logout():
      return "logout"



class User(db.Document):
    email = db.StringField(max_length=50)
    password = db.StringField(max_length=50)

class Data(db.Document):
    subject = db.StringField(max_length=500)
    text_data = db.StringField(max_length=1000)
    date = db.StringField(max_length=100)

if __name__ == '__main__':
    app.run()
