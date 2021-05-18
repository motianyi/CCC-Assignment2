from flask import Flask
from flask import request
from flask import render_template
import utils

app = Flask(__name__, static_folder="/")


@app.route('/')
def main():
    return render_template('main.html')
	
# @app.route('/time')
# def get_time():
# 	return utils.get_time()

# @app.route('/map.html')
# def map():
#     return render_template('map.html')


if __name__ == '__main__':
    app.run(debug = True)
