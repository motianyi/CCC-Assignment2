from flask import Flask
from flask import request
from flask import render_template, send_from_directory
import utils
import os

app = Flask(__name__,
            static_url_path='', 
            static_folder='',
            template_folder='templates')


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/overview.html')
def overview():
    return render_template('overview.html')

@app.route('/covid.html')
def covid():
    return render_template('covid.html')

@app.route('/heal-con.html')
def heal():
    return render_template('heal-con.html')

@app.route('/income.html')
def income():
    return render_template('income.html')

@app.route('/ente.html')
def ente():
    return render_template('ente.html')

@app.route('/lang.html')
def lang():
    return render_template('lang.html')


if __name__ == '__main__':
    app.run(debug = True)