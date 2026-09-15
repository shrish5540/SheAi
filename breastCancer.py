import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

# Initializing the Flask application
app = Flask(__name__)
breastCancer = pickle.load(open('breastCancer.pkl', 'rb'))


# Defining the route for the home page
@app.route('/')
def home():
  print("ixjisjxisjx")
  return render_template('breastCancer.html')



# Defining the route for breast cancer prediction (handles POST requests)
@app.route('/predictcancer',methods=['POST'])
def predictCancer():
  # Extracting input features from the form submitted by the user
  input_features = [int(x) for x in request.form.values()]
  features_value = [np.array(input_features)]

  # Defining the feature names expected by the model
  features_name = ['clump_thickness', 'uniform_cell_size', 'uniform_cell_shape',
       'marginal_adhesion', 'single_epithelial_size', 'bare_nuclei',
       'bland_chromatin', 'normal_nucleoli', 'mitoses']

    # Creating a DataFrame from the input values to match model requirements
  df = pd.DataFrame(features_value, columns=features_name)
  output = breastCancer.predictCancer(df)

  if output == 4:
      res_val = "We understand that this information may be concerning. Based on the analysis, there are indications of breast malignancy"
  else:
      res_val = "Based on the analysis, there are no indications of breast malignancy."
  
   # Rendering the result on the HTML page
  return render_template('breastCancer.html', prediction_text='{}'.format(res_val))

# Running the Flask application
if __name__ == "__main__":
  app.run()
