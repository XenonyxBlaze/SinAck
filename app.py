from flask import Flask, render_template
from flask_cors import CORS

import os

import goodsniffer

import multiprocessing

app = Flask("SinAck") 
CORS(app)

global scan_status
global scan_link

scan_status = "Start Scan"
scan_link = "/scan"

app.config.update( 
    SECRET_KEY='dev'
)

@app.route('/')
def index_function():
    return render_template('index.html', scanbtn=scan_status, scanlink=scan_link)
    

@app.route('/scan')
def scan_function():
    global snifferProcess
    snifferProcess = multiprocessing.Process(target=goodsniffer.main)
    snifferProcess.start()
    global scan_status
    global scan_link
    scan_status = "Stop Scan"
    scan_link = "/stopscan"
    return app.redirect('/')

@app.route('/stopscan')
def stop_scan():
    snifferProcess.terminate()
    global scan_status
    global scan_link
    scan_status = "Start Scan"
    scan_link = "/scan"
    return app.redirect('/')

# @app.route('/stopscan')
# def stop_scan_function():



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80, threaded=True)