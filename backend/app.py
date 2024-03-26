# backend/app.py
# defines my API routes
# defines route for calculating caloric needs using Wt, Ht and age

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"], headers=['Content-Type']) 

@app.route('/process-data', methods=['POST'])
def process_data():
    data = request.json
    weight = data.get('weight')
    height = data.get('height')
    age = int(data.get('age'))

    if age < 6 or age > 23:
        return jsonify({'error': 'This system only works for kids aged 6-23 months old.'}), 400

    # to call the expert system logic to process the input data
    recommendations, feedback = process_with_expert_system(weight, height, age)

    return jsonify({'recommendations': recommendations, 'feedback': feedback})

def process_with_expert_system(weight, height, age):
    # Calculate Z-scores for weight-for-age, height-for-age, and weight-for-height
    weight_for_age_z_score = calculate_weight_for_age_z_score(weight, age)
    height_for_age_z_score = calculate_height_for_age_z_score(height, age)
    weight_for_height_z_score = calculate_weight_for_height_z_score(weight, height)

    # Provide nutrition feedback based on Z-scores
    feedback = ""
    feedback += "Nutritional status:<br>"
    feedback += f"Weight-for-age Z-score: {weight_for_age_z_score}<br>"
    feedback += f"Height-for-age Z-score: {height_for_age_z_score}<br>"
    feedback += f"Weight-for-height Z-score: {weight_for_height_z_score}<br>"
    if weight_for_age_z_score < -2:
        feedback += "The child is underweight.<br>"
    if height_for_age_z_score < -2:
        feedback += "The child is stunted.<br>"
    if weight_for_height_z_score < -2:
        feedback += "The child has wasting.<br>"

    # For demonstration purposes
    recommendations = 'Sample food recommendations'

    return recommendations, feedback

def calculate_weight_for_age_z_score(weight, age):
    z_score = 0  # Placeholder value, to replace with actual calculation
    return z_score

def calculate_height_for_age_z_score(height, age):
    z_score = 0  # Placeholder value, to replace with actual calculation
    return z_score

def calculate_weight_for_height_z_score(weight, height):
    z_score = 0  # Placeholder value, to replace with actual calculation
    return z_score


if __name__ == '__main__':
    app.run(debug=True)



def calculate_weight_for_age_z_score(weight, age):
    z_score = 0  # Placeholder value, to replace with actual calculation
    return z_score

def calculate_height_for_age_z_score(height, age):
    z_score = 0  # Placeholder value, to replace with actual calculation
    return z_score

def calculate_weight_for_height_z_score(weight, height):
    z_score = 0  # Placeholder value, to replace with actual calculation
    return z_score


if __name__ == '__main__':
    app.run(debug=True)

