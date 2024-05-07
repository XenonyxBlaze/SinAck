from flask import Flask, render_template
from flask_cors import CORS

app = Flask("SinAck") 
CORS(app)

app.config.update( 
    SECRET_KEY='dev'
)

@app.route('/')
def index_function(): 
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80, threaded=True)