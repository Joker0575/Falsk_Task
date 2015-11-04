from flask import Flask,redirect
from flask import render_template
from flask import g
from flask import request
from flask import request, jsonify
from flask.ext.mongoengine import MongoEngine
from textblob import TextBlob


app = Flask(__name__)


app.config['MONGODB_SETTINGS'] = {
    'db': 'twitter_analysis',
    'host': 'localhost',
    'port': 27017
}

db = MongoEngine(app)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(email="abc",password='rajkoti05@gmail.com ')
        user.save()
        return redirect("/application", code=302)
    return render_template('index.html')


@app.route('/application',methods=['GET', 'POST'])
def application():
    if request.method == 'POST':
        data = Data(subject="test",text_data='rajkoti05@gmail.com ')
        data.save()
        return redirect("/submitted_data", code=302)
    return render_template('app.html')

@app.route('/submitted_data',methods=['GET', 'POST'])
def submitted_data():
    return render_template('submitted.html')


@app.route('/logout',methods=['GET'])
def logout():
      return "logout"



class User(db.Document):
    email = db.StringField(max_length=500)
    password = db.StringField(max_length=1000)

class Data(db.Document):
    subject = db.StringField(max_length=500)
    text_data = db.StringField(max_length=1000)

if __name__ == '__main__':
    app.run()
