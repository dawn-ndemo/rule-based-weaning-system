from flask import Flask, request, jsonify
from flask_cors import CORS
from rules import FeedingExpert

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

    # Create an instance of the FeedingExpert class
    expert = FeedingExpert()

    # Get recommendations from the expert system
    recommendations = expert.get_recommendations(age)

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

    # Include recommendations from the expert system
    feedback += "<br><b>Expert System Recommendations:</b><br>"
    feedback += recommendations

    return jsonify({'recommendations': recommendations, 'feedback': feedback})

# Placeholder functions for calculating Z-scores --- considering not doing z-scores after all
def calculate_weight_for_age_z_score(weight, age):
    z_score = 0  # Placeholder value
    return z_score

def calculate_height_for_age_z_score(height, age):
    z_score = 0  # Placeholder value
    return z_score

def calculate_weight_for_height_z_score(weight, height):
    z_score = 0  # Placeholder value
    return z_score

if __name__ == '__main__':
    app.run(debug=True)
