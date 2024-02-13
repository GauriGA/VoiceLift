from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load(open('finalised_model.sav', 'rb'))

def convert_to_float(string):
    # Split the string by the '-' character
    parts = string.split('-')
    
    # Convert each part to a float
    lower_bound = float(parts[0].strip())
    upper_bound = float(parts[1].strip()[:-5])  # Removing ' year' from the upper bound
    
    # Calculate the average
    average = (lower_bound + upper_bound) / 2.0
    
    return average

@app.route('/')
def home():
    return render_template('modelindex.html')

@app.route('/result')
def result():
    return render_template('result.html', result=request.args.get('result'))

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    age = request.form['age']
    if age == 'More than 30 years':
        age_numeric = 0
    else:
        age_numeric = convert_to_float(age)  # Convert age string to numeric value
    
    sex = request.form['sex']
    if sex == 'Male':
        sex=1
    else:
        sex = 0
    occupation = request.form['occupation']
    indoor_days = request.form['indoor_days']
    stress_growth = request.form['stress_growth']
    frustration = request.form['frustration']
    habit_changes = request.form['habit_changes']
    mental_health_history = request.form['mental_health_history']
    weight_changes = request.form['weight_changes']
    mood_swings_frequency = request.form['mood_swings_frequency']
    coping_struggles = request.form['coping_struggles']
    interest_in_working = request.form['interest_in_working']
    social_weakness = request.form['social_weakness']

    if occupation == 'Corporate':
        occupation = 0
    elif occupation == 'Student':
        occupation = 1
    elif occupation == 'Housewife':
        occupation = 2
    elif occupation == 'Business':
        occupation = 3
    else:
        occupation = 4  # Others

    # Convert indoor_days to numerical values
    if indoor_days == '1-14 days':
        indoor_days = 0
    elif indoor_days == '15-30 days':
        indoor_days = 1
    elif indoor_days == '30-61 days':
        indoor_days = 2
    elif indoor_days == 'More than 2 months':
        indoor_days = 3
    else:
        indoor_days = 4  # Go outside daily

    # Convert stress_growth to numerical values
    if stress_growth == 'Yes':
        stress_growth = 1
    elif stress_growth == 'No':
        stress_growth = 0
    else:
        stress_growth = 2  # Maybe

    # Convert frustration to numerical values
    if frustration == 'Yes':
        frustration = 1
    elif frustration == 'No':
        frustration = 0
    else:
        frustration = 2  # Maybe

    # Convert habit_changes to numerical values
    if habit_changes == 'Yes':
        habit_changes = 1
    elif habit_changes == 'No':
        habit_changes = 0
    else:
        habit_changes = 2  # Maybe

    # Convert mental_health_history to numerical values
    if mental_health_history == 'Yes':
        mental_health_history = 1
    elif mental_health_history == 'No':
        mental_health_history = 0
    else:
        mental_health_history = 2  # Maybe

    # Convert weight_changes to numerical values
    if weight_changes == 'Yes':
        weight_changes = 1
    elif weight_changes == 'No':
        weight_changes = 0
    else:
        weight_changes = 2  # Maybe

    # Convert mood_swings_frequency to numerical values
    if mood_swings_frequency == 'High':
        mood_swings_frequency = 2
    elif mood_swings_frequency == 'Medium':
        mood_swings_frequency = 1
    else:
        mood_swings_frequency = 0  # Low

    # Convert coping_struggles to numerical values
    if coping_struggles == 'Yes':
        coping_struggles = 1
    else:
        coping_struggles = 0

    # Convert interest_in_working to numerical values
    if interest_in_working == 'Yes':
        interest_in_working = 1
    elif interest_in_working == 'No':
        interest_in_working = 0
    else:
        interest_in_working = 2  # Maybe

    # Convert social_weakness to numerical values
    if social_weakness == 'Yes':
        social_weakness = 1
    elif social_weakness == 'No':
        social_weakness = 0
    else:
        social_weakness = 2  # Maybe

    # Create a list of features
    features = [age_numeric, sex, occupation, indoor_days, stress_growth, frustration, habit_changes, mental_health_history, weight_changes, mood_swings_frequency, coping_struggles, interest_in_working, social_weakness]
    
    # Call predict method on the model
    prediction = model.predict([features])[0]

    # Redirect to the result route with the prediction result as a parameter
    return redirect(url_for('result', result=prediction))

if __name__ == '__main__':
    app.run(debug=True)
