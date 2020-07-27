import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__,static_url_path='/static')
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')
	
@app.route('/emi')
def emi():
    return render_template('emi.html')
	
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    if output == 1:
        return render_template('index.html', prediction_text='Loan Status: {}'.format("Congratulations! You are eligible for this loan."))
    elif output == 0:
        return render_template('index.html', prediction_text='Loan Status: {}'.format("Sorry! You are not eligible for this loan.")) 

    

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)