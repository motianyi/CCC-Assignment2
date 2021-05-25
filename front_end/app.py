from flask import Flask
from flask import request
from flask import render_template, send_from_directory
# import utils


app = Flask(__name__,
            static_url_path='', 
            static_folder='',
            template_folder='templates')


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/overview-visualization.html')
def overview():
    return render_template('overview-visualization.html')

@app.route('/covid-visualization.html')
def covid():
    return render_template('covid-visualization.html')

@app.route('/health-visualization.html')
def health():
    return render_template('health-visualization.html')

@app.route('/financial-visualization.html')
def financial():
    return render_template('financial-visualization.html')

if __name__ == '__main__':
    app.run(debug = True)
