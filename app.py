from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("daibites.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Corrected typo: np.array (you had np.arrray)
        input_data = [float(x) for x in request.form.values()]
        data = np.array([input_data])
        
        prediction = model.predict(data)[0]
        result = "Diabetic" if prediction == 1 else "Not Diabetic"
        
        return render_template("index.html", prediction_text=f'Result: {result}')
    
    except Exception as e:
        print("DEBUG ERROR:", e)  # Print error to terminal/log for debugging
        return render_template("index.html", prediction_text="Invalid input")

if __name__ == "__main__":
    app.run(debug=True)
