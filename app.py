from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# -----------------------
# Load trained model
# -----------------------

model = joblib.load("best_model_heart.pkl")


# -----------------------
# Home page
# -----------------------

@app.route("/")
def home():
    return render_template("index.html")


# -----------------------
# Prediction function
# -----------------------

@app.route("/predict", methods=["POST"])
def predict():

    try:

        age = float(request.form["age"])
        sex = int(request.form["sex"])
        chest_pain = int(request.form["chest_pain"])
        bp = float(request.form["bp"])
        cholesterol = float(request.form["cholesterol"])
        ekg = int(request.form["ekg"])
        max_hr = float(request.form["max_hr"])
        exercise_angina = int(request.form["exercise_angina"])
        st_depression = float(request.form["st_depression"])
        slope = int(request.form["slope"])
        vessels = int(request.form["vessels"])
        thallium = int(request.form["thallium"])

        # create input array
        data = np.array([[age, sex, chest_pain, bp, cholesterol,
                          ekg, max_hr, exercise_angina,
                          st_depression, slope, vessels, thallium]])

        # prediction
        prediction = model.predict(data)

        if prediction[0] == 1:
            result = "Heart Disease Detected"
        else:
            result = "No Heart Disease"

    except Exception as e:
        result = "Error: " + str(e)

    return render_template("index.html", prediction_text=result)


# -----------------------
# Run Flask app
# -----------------------

if __name__ == "__main__":
    app.run(debug=True)