from flask import Flask
import bente_app

app = Flask(__name__)
 
@app.route('/')
def home():
    return "This is the home page"


@app.route('/bente')
def bente():
    result = bente_app.krijg_output()
    print(result)
    return "tweede return" + result


 
if __name__ == '__main__':
    app.run(debug=True)