from flask import Flask,request, jsonify,render_template
import pickle
import numpy as np
#load trained model
model_path='insurance__model.pkl'
with open(model_path,'rb') as file:
    model=pickle.load(file)
app=Flask(__name__)
@app.route('/')
def home():
    prediction=None
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['POST'])
def predict():

    age = request.form.get('age')
    gender = request.form.get('gender')
    bmi = request.form.get('bmi')
    children = request.form.get('children')
    smoker = request.form.get('smoker')
    region = request.form.get('region')

    # if any field missing → return page without prediction
    if not age or not gender or not bmi or not children or not smoker or not region:
        return render_template("index.html", prediction=None)

    age = int(age)
    bmi = float(bmi)
    children = int(children)

    region_map = {
        "southwest":0,
        "southeast":1,
        "northwest":2,
        "northeast":3
    }

    region = region_map[region]
    gender = 1 if gender == "male" else 0
    smoker = 1 if smoker == "yes" else 0

    features = [age, gender, bmi, children, smoker, region]

    prediction = model.predict([features])[0]
    prediction = "{:,.2f}".format(prediction)

    return render_template("index.html", prediction=prediction)
if __name__=="__main__":
    app.run(debug=True)