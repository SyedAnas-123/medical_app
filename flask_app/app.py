from flask import Flask, request, render_template
import pickle
import numpy as np

# Load the trained diabetes model
model_path = 'model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from form
    gender = request.form['gender']
    gender_numeric = 1 if gender.lower() == 'male' else 0  # Male = 1, Female = 0

    input_data = [gender_numeric] + [1 if x.lower() == 'yes' else 0 if x.lower() == 'no' else int(x) for x in list(request.form.values())[1:]]
    final_features = [np.array(input_data)]
    
    # Make prediction
    prediction = model.predict(final_features)
    
    if prediction[0] == 1:
        output = "⚠️ Based on your inputs, you may be at high risk for diabetes. Please consult your doctor."
    else:
        output = "✅ Your inputs suggest that you have a low risk of diabetes. Stay healthy!"
    
    return render_template('index.html', prediction_text=output)

if __name__ == "__main__":
    app.run(debug=True)
