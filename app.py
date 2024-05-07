from flask import Flask, render_template
from flask_cors import CORS

import goodsniffer

app = Flask("SinAck") 
CORS(app)

app.config.update( 
    SECRET_KEY='dev'
)

@app.route('/')
def index_function(): 
    return render_template('index.html')

@app.route('/scan')
def scan_function():
    goodsniffer.main


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80, threaded=True)