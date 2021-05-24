from flask import Flask
from flask import request
from flask import render_template
import utils

app = Flask(__name__, static_url_path="/")

@app.route('/')
def home():
    return app.send_static_file('home.html')

# @app.route('/map')
# def map():
#     return '../ccc-asn2-grp31/template'

if __name__ == '__main__':
    app.run(debug = True)
