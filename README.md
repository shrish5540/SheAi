# Her-AI Assist - AI for Women's Health

## Overview
✨ **Her-AI Assist** is an AI-driven platform designed to provide women with personalized health insights. By utilizing advanced machine learning models 🤖, it tackles critical health issues like pregnancy complications 🤰, PCOS (Polycystic Ovary Syndrome), and breast cancer 🎗️. The platform aims to improve access to timely medical support and empower women with informed healthcare decisions 💪.

![HERAI](https://github.com/user-attachments/assets/15ff0faf-36ce-4b3c-b83f-bc11e775f064)

## The Challenge
🌍 In many regions, especially low-income areas, women face significant barriers to healthcare access. Over 60% of women are unable to receive the care they need, leading to preventable complications during pregnancy 🤰, undiagnosed PCOS 🌸, and late-stage cancer diagnoses 🎗️. This gap highlights the urgent need for an AI-powered solution that can provide accurate, timely health assistance 💡.

### Key Statistics:
- **Pregnancy**: 210 million pregnancies occur annually, with 20 million facing complications (WHO). Over 60% of women in low-income settings lack access to essential care.
- **Menstrual Health**: 75% of adolescent girls suffer from menstrual disorders, many due to misinformation (ACOG).
- **Pregnancy Risks**: 830 women die every day due to pregnancy-related complications, with 94% of these deaths in low-resource settings (WHO).
- **PCOS**: PCOS affects 10% of women of reproductive age, but 70% remain undiagnosed (PCOS Awareness Association).
- **Breast Cancer**: Leading cause of cancer-related deaths among women. Early detection increases survival rates by 90% (BCRF).

- 
  ![image](https://github.com/user-attachments/assets/ed714bb8-11df-492f-89ca-34bd51c0aa69)



## Solution
Her-AI Assist leverages cutting-edge AI models to address these pressing health concerns. The platform offers:
1. **Pregnancy Risk Detection**: Predicts pregnancy-related risks based on health data like age, BMI, blood pressure, and glucose levels.
2. **PCOS Detection**: Identifies potential PCOS cases by analyzing hormonal data, cycle irregularities, and BMI.
3. **Breast Cancer Detection**: Uses mammographic data to classify tumors, facilitating early cancer detection.
4. **AI Chatbot**: A chatbot powered by NLP, providing real-time, personalized responses to a wide range of women’s health inquiries.
   
![image](https://github.com/user-attachments/assets/0dba955a-98ad-4de9-953c-938990cbcd20)

![image](https://github.com/user-attachments/assets/2ba8b89d-965f-4529-ab93-3e5bd8487f35)

## Features
- **Pregnancy Risk Assessment**: Enter maternal health data (age, BMI, glucose levels) for pregnancy risk prediction.
- **PCOS Prediction**: Provide hormonal data and cycle information to assess the likelihood of PCOS.
- **Breast Cancer Detection**: Upload mammographic images for tumor classification.
- **AI Health Chatbot**: Ask any health-related questions and get instant, tailored responses.

## Data Used
- **Pregnancy Risk**: Maternal Health Risk dataset from UCI.
- **PCOS Detection**: Data on hormonal levels, cycle patterns, and BMI.
- **Breast Cancer Detection**: Mammographic dataset with features such as radius, texture, and compactness.

## Installation
# Setting Up the Virtual Environment

Follow the steps below to create and activate a virtual environment for your project.

## Step 1: Install `virtualenv` (if not already installed)

To create a virtual environment, you need to have `virtualenv` installed. Run the following command to install it:

```bash
pip install virtualenv
```
## Step 2: Create the Virtual Environment
Navigate to your project directory and run the following command to create the virtual environment:

```bash
virtualenv venv
```
This will create a folder named venv that contains the isolated virtual environment.

## Step 3: Activate the Virtual Environment

#Command Prompt (CMD):
```bash
.\venv\Scripts\activate
```
#PowerShell:
```bash
.\venv\Scripts\activate.ps1
```
On macOS/Linux:
```bash
source venv/bin/activate
```
Once activated, you should see the virtual environment name (venv) in your terminal prompt.
# Requirements

## 1. Python Environment
- Python 3.7 or higher.

## 2. Dependencies
Install the following dependencies for the project. You can install them using the `requirements.txt` file.

### Essential Packages:
- `blinker==1.9.0`: For message-passing and signals.
- `click==8.1.8`: For creating command-line interfaces.
- `colorama==0.4.6`: For colorizing terminal text.
- `flask==3.1.0`: For building the web application backend.
- `matplotlib`: For plotting and visualizing data.
- `google.generativeai`: For interacting with Google's generative AI API.
- `gunicorn==23.0.0`: For running the Flask app in production.
- `itsdangerous==2.2.0`: For cryptographic operations in Flask.
- `Jinja2==3.1.5`: For templating engine in Flask.
- `joblib==1.4.2`: For serializing Python objects.
- `MarkupSafe==3.0.2`: For safely handling untrusted input in templates.
- `numpy==1.26.4`: For numerical operations and array handling.
- `packaging==24.2`: For package version handling.
- `pandas==2.2.2`: For data manipulation and analysis.
- `python-dateutil==2.9.0.post0`: For date parsing and manipulation.
- `pytz==2025.1`: For timezone handling.
- `scipy==1.15.1`: For scientific and technical computing.
- `six==1.17.0`: For compatibility between Python 2 and 3.
- `threadpoolctl==3.5.0`: For controlling the threadpool used by libraries.
- `tzdata==2025.1`: For handling timezone data.
- `Werkzeug==3.1.3`: For working with WSGI applications in Flask.
- `scikit-learn==1.6.1`: For machine learning algorithms and tools.
- `sklearn`: For machine learning tools and utilities.
- `pickle`: For serializing Python objects.

### Optional Packages:
- `pytest`: For running unit tests on the application.

## Step 4: Install Dependencies
Install the project dependencies from the requirements.txt file:

```bash
pip install -r requirements.txt
```
This will install all the necessary libraries for the project.


## Step 5: Get the Google Studio API Key

To get your Google Studio API key, follow these steps:

1. Visit the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing project.
3. Go to the **APIs & Services** dashboard.
4. Click on **Enable APIs and Services**.
5. Search for **Google Cloud AI** or **Google Studio API** and enable it.
6. Navigate to **Credentials** in the left sidebar.
7. Click on **Create Credentials**, then select **API Key**.
8. Copy the generated API key. You will use this in the next step.

## Step 6: Insert the API Key into `her_chatbot.py`

Once you have the API key, insert it into your `her_chatbot.py` file. 

1. Open the `her_chatbot.py` file in a text editor.
2. Find the line where the API key is required. It should look something like this:


3. Replace `"API_KEY"` with your actual API key:

    ```python
    API_KEY = "YOUR_ACTUAL_API_KEY"  # Replace with your real Google Studio API key
    ```

4. Save the `her_chatbot.py` file.

Now your chatbot should be configured to interact with the Google Studio API, utilizing the key you've integrated.

## Step 5: Start the App
Now that the virtual environment is activated and dependencies are installed, run the application:
```
bash
python app.py
```
Your app should now be running locally. You can access it by navigating to http://127.0.0.1:5001/ in your web browser.

#FILE STRUCTURE 
```
HER-AI/
├── __pycache__/
├── static/
│   ├── css/
│   ├── img/
│   ├── js/
│   ├── lib/
│   ├── php/
│   └── scss/
├── templates/
│   ├── about.html
│   ├── bot.html
│   ├── breastCancer.html
│   ├── check.html
│   ├── contact.html
│   ├── index.html
│   ├── pcos.html
│   ├── price.html
│   ├── service.html
│   ├── team.html
│   └── testimonial.html
├── .gitignore
├── app.py
├── Breast_Cancer_Detection.ipynb
├── breastCancer.pkl
├── breastCancer.py
├── feature_order.pkl
├── her_chatbot.py
├── model.pkl
├── pcos_app.py
├── README.md
├── requirements.txt
├── rf_model.pkl
└── scaler.pkl
```
# Collaterals of the Code

## Backend Code:
- **app.py**: Main application file for Flask backend.
- **her_chatbot.py**: AI-powered chatbot implementation.
- **pcos_app.py**: PCOS detection model integration.

## Model Files:
- **breastCancer.pkl**: Trained breast cancer detection model.
- **feature_order.pkl**: Feature order for model input.
- **model.pkl**: General predictive model.
- **rf_model.pkl**: Random Forest model.
- **scaler.pkl**: Scaler for data preprocessing.

## HTML Templates:
The files in the `templates/` directory provide the frontend user interface for different sections of the application:
- **about.html**
- **bot.html**
- **breastCancer.html**
- **check.html**
- **contact.html**
- **index.html**
- **pcos.html**
- **price.html**
- **service.html**
- **team.html**
- **testimonial.html**

## Data Storage:
- **requirements.txt**: List of dependencies for the project.
- **README.md**: Project documentation and instructions.

## Notebooks:
- **Breast_Cancer_Detection.ipynb**: Jupyter notebook for breast cancer model development.

## Future Directions
- **Broaden the Scope**: Introduce new healthcare conditions to the platform.
- **Partnerships**: Work with clinics and healthcare providers for broader reach.
- **Ongoing Model Improvement**: Keep updating models with new data and real-world scenarios to enhance accuracy.

## Contributing
If you'd like to contribute, feel free to submit pull requests or report issues. Your improvements and ideas are always welcome!

## License
This project is licensed under the MIT License. 

## Acknowledgements
- **WHO** and **UCI** for providing the datasets.
- **TensorFlow**, **Keras**, and **Scikit-learn** for the machine learning tools.
- **Flask** for powering the backend of the web application.

## Model Overview
- **AI-Powered Chatbot**: Trained using NLP transformer models based on health FAQs and medical research to provide personalized, context-aware answers. It incorporates intent recognition, entity extraction, and reinforcement learning for improved response quality.
- **Pregnancy Risk Model**: A classification model (XGBoost, Random Forest) trained on maternal health data (age, BMI, glucose levels). It utilizes SHAP for model interpretability, highlighting key risk factors.
- **PCOS Detection Model**: A binary classification model (SVM, XGBoost) using features like hormonal levels, cycle regularities, BMI, and insulin resistance. It applies recursive feature elimination (RFE) and LIME for better interpretability.
- **Breast Cancer Detection Model**: Analyzes mammographic data using XGBoost and Neural Networks (EfficientNet, ResNet) to classify tumors. It processes features such as radius, texture, and compactness. Transfer learning and ensemble techniques further optimize performance.

## Testing & Evaluation
- **Model Evaluation**: Cross-validation, user feedback, load testing, and integration checks are performed to ensure robust performance.
- **Real-World Applicability**: Edge cases and data handling scenarios are tested to ensure the platform’s effectiveness in real-world conditions.
