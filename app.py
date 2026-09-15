from flask import Flask, request, render_template, jsonify,redirect,url_for
import subprocess
import numpy as np
import pandas as pd
import joblib
import threading
from her_chatbot import chat_session
from pcos_app import model
import pickle

# Initialize the Flask application
app = Flask(__name__, static_folder='static', template_folder='templates')

# Load the trained model and scaler
xgb_model = joblib.load('rf_model.pkl')
scaler = joblib.load('scaler.pkl')
breastCancer = pickle.load(open('breastCancer.pkl', 'rb'))

# Define normal ranges for pregnancy-related health parameters
pregnancy_normal_ranges = {
    "Age": (18, 35),
    "Body Temperature(F)": (97, 99),
    "Heart rate(bpm)": (70, 110),
    "Systolic Blood Pressure(mm Hg)": (65, 140),
    "Diastolic Blood Pressure(mm Hg)": (70, 80),
    "BMI(kg/m 2)": (18.5, 24.9),
    "Blood Glucose(HbA1c)": (0, 42),  # Upper limit for HbA1c
    "Blood Glucose(Fasting hour-mg/dl)": (3.3, 5.1),
}

# Map prediction outcome to risk levels
def risk_level(outcome):
    levels = {0: "Low Risk", 1: "Medium Risk", 2: "High Risk"}
    return levels.get(outcome, "Unknown Risk")

# Function to explain risk factors based on input values
def explain_risk_factors(user_input):
    explanations = []
    for feature, value in user_input.items():
        if feature in pregnancy_normal_ranges:
            low, high = pregnancy_normal_ranges[feature]
            if value < low:
                explanations.append(f"Low {feature} ({value})")
            elif value > high:
                explanations.append(f"High {feature} ({value})")
    return explanations

# Define routes for rendering HTML templates
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/price')
def price():
    return render_template('price.html')

@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')

@app.route('/check', methods=['GET'])
def check():
    return render_template('check.html', result=None, explanations=None)


# Route to handle form submission for health risk assessment
@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Get form inputs
        age = float(request.form['Age'])
        height = float(request.form['height'])  
        weight = float(request.form['weight'])  
        body_temp = float(request.form['Body_Temperature'])
        heart_rate = float(request.form['Heart_Rate'])
        systolic_bp = float(request.form['Systolic_BP'])
        diastolic_bp = float(request.form['Diastolic_BP'])
        blood_glucose_hba1c = float(request.form['Blood_Glucose_HbA1c'])
        blood_glucose_fasting = float(request.form['Blood_Glucose_Fasting'])

        # Calculate BMI
        bmi = weight / ((height / 100) ** 2)

        # Prepare input data
        user_input = {
            "Age": age,
            "Body Temperature(F) ": body_temp,
            "Heart rate(bpm)": heart_rate,
            "Systolic Blood Pressure(mm Hg)": systolic_bp,
            "Diastolic Blood Pressure(mm Hg)": diastolic_bp,
            "BMI(kg/m 2)": bmi,
            "Blood Glucose(HbA1c)": blood_glucose_hba1c,
            "Blood Glucose(Fasting hour-mg/dl)": blood_glucose_fasting
        }

        feature_order = [
            "Age", "Body Temperature(F) ", "Heart rate(bpm)", 
            "Systolic Blood Pressure(mm Hg)", "Diastolic Blood Pressure(mm Hg)",
            "BMI(kg/m 2)", "Blood Glucose(HbA1c)", "Blood Glucose(Fasting hour-mg/dl)"
        ]

        # Scale and prepare input for the model
        input_array = [[user_input[feature] for feature in feature_order]]
        input_scaled = scaler.transform(input_array)
        input_df = pd.DataFrame(input_scaled, columns=feature_order)

     
        # Make prediction using the model
        predicted_outcome = int(xgb_model.predict(input_df))  # Ensure integer output
        risk = risk_level(predicted_outcome)

        # Explanation
        explanations = explain_risk_factors(user_input)

        result = {
            "prediction": risk,
            "explanations": explanations
        }
        return render_template('check.html', result=result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400



# Route to start PCOS analysis script in a separate thread
@app.route('/pcos_run')
def pcos_run():
    threading.Thread(target=lambda: subprocess.run(["python", "pcos_app.py"])).start()
    return redirect(url_for('pcos'))

# Route to predict PCOS
@app.route('/pcos')
def pcos():
    return render_template('pcos.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    if prediction == 1:
        return render_template('pcos.html', prediction_text='The Person has PCOS with the accuracy of 90.79%')
    else:
        return render_template('pcos.html', prediction_text='The Person does not have PCOS with the accuracy of 90.79%')


# Route to start chatbot script

@app.route('/run_chatbot', )
def run_chatbot():
    threading.Thread(target=lambda: subprocess.run(["python", "her_chatbot.py"])).start()
    return redirect(url_for('bot'))

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.form["message"]
    print(f"Received message: {user_message}")  # Debug print
    if user_message:
        response = chat_session.send_message(user_message)
        bot_reply = response.text
        print(f"Bot reply: {bot_reply}")  # Debug print
        return jsonify({"response": bot_reply})
    return jsonify({"response": "Please enter a message."})

@app.route('/predictcancer', methods=['GET'])
def predictcancer():
    return render_template('breastCancer.html')


@app.route('/predictcancer', methods=['POST'])
def predictCancer():
    input_features = [(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    
    features_name = ['clump_thickness', 'uniform_cell_size', 'uniform_cell_shape',
                     'marginal_adhesion', 'single_epithelial_size', 'bare_nuclei',
                     'bland_chromatin', 'normal_nucleoli', 'mitoses']
    
    df = pd.DataFrame(features_value, columns=features_name)
    # Use the correct predict method
    output = breastCancer.predict(df)
    
    # Since scikit-learn returns an array, you may want to access the first element
    prediction = output[0] if hasattr(output, '__iter__') else output

    if prediction == 4:
        res_val = ("We understand that this information may be concerning. "
                   "Based on the analysis, there are indications of BREAST MALIGANCY")
    else:
        res_val = ("Based on the analysis, there are NO indications of breast malignancy.")
    
    return render_template('breastCancer.html', prediction_text=res_val)

# Route for chatbot interaction
@app.route('/bot')
def bot():
    return render_template('bot.html')

import os

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5001)), debug=False)
# Run Flask app

