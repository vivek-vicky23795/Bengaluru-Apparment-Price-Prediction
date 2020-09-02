import flask
from flask import request
app = flask.Flask(__name__)
app.config["DEBUG"] = True

from flask_cors import CORS
CORS(app)


@app.route('/',methods=['GET'])
def default():
    return ''' <h1> Helloo.  Data scientist 22-JUL 2020 Batch </h1>'''

@app.route('/vivek',methods=['GET'])
def vivek():
    return ''' <h1> From Aspiring DataScientist to DataScientist....... </h1>'''



@app.route('/corona',methods=['GET'])
def corona():
    return ''' <h1> Corona curve is NOT flattening..  it is rising exponentially </h1>'''

@app.route('/search',methods=['GET'])
def search():
    return ''' <h1> Searching...  '''+ request.args['s']+ '''</h1>'''



@app.route('/predict',methods=['GET'])
def predict():
    import joblib
    model = joblib.load('House_Price_prediction-01-09-2020.pkl')
    price = model.predict([[int(request.args['sqft']),
                            int(request.args['place']),
                            int(request.args['yo']),
                            int(request.args['tf']),
                            int(request.args['bhk']),
                           ]])
    return str(round(price[0]))


app.run()
