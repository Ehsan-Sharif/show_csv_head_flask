from app import app
from flask import render_template


@app.route('/')
def home():
    return "hello world!"


@app.route('/airbase')
def AIR_HEAD():
    return render_template('airbase.html')


@app.route('/titanic')
def Titanic_HEAD():
    return render_template('titanic.html')


@app.route('/flow')
def flow_HEAD():
    return render_template('flow.html')


@app.route('/melb')
def Melb_HEAD():
    return render_template('melb.html')
