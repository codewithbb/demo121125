from flask import Flask
import bente_app
from abel_connect import extract_rows_tabel
import donny_app
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "This is the home page"

@app.route('/bente')
def bente():
    result = bente_app.krijg_output()
    print(result)
    return result


@app.route('/abel')
def abel():
   output_abel = extract_rows_tabel('test_tabel')
   return output_abel


@app.route('/donny/')
def donny():
   output_donny = donny_app.krijg_output("heel_leuk")
   return output_donny


if __name__ == '__main__':
    app.run(debug=True)