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
    # The expert system logic to go here...to replace this with the actual logic to generate food recommendations and feedback
    recommendations = 'Sample food recommendations'
    feedback = 'Sample nutrition feedback'
    return recommendations, feedback

if __name__ == '__main__':
    app.run(debug=True)

