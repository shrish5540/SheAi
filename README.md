# She-AI Assist - AI for Women's Health

## Overview
✨ **She-AI Assist** is an AI-driven platform designed to provide women with personalized health insights. By utilizing advanced machine learning models 🤖, it tackles critical health issues like pregnancy complications 🤰, PCOS (Polycystic Ovary Syndrome), and breast cancer 🎗️. The platform aims to improve access to timely medical support and empower women with informed healthcare decisions 💪.

![SheAI](https://github.com/user-attachments/assets/15ff0faf-36ce-4b3c-b83f-bc11e775f064)

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
She-AI Assist leverages cutting-edge AI models to address these pressing health concerns. The platform offers:
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
