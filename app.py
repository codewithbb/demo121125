from flask import Flask
import bente_app
from abel_connect import extract_rows_tabel

app = Flask(__name__)

@app.route('/')
def home():
    return "This is the home page"

@app.route('/bente')
def bente():
    result = bente_app.krijg_output()
    print(result)
    return "tweede return" + result

@app.route('/abel')
def abel():
   output_abel = extract_rows_tabel('test_tabel')
   print(output_abel)
   return "abel executed successfully: " + str(output_abel)

if __name__ == '__main__':
    app.run(debug=True)