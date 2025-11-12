from flask import Flask
from abel_connect import extract_rows_tabel
from flask import jsonify


app = Flask(__name__)
 
@app.route('/')
def home():
    return "This is the home page"

@app.route('/abel')
def abel():
   output_abel = extract_rows_tabel('test_tabel')
   return output_abel


if __name__ == '__main__':
    app.run(debug=True)