from flask import Flask, request, jsonify
from flask_cors import CORS
from rules import FeedingExpert

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"], headers=['Content-Type']) 

@app.route('/process-data', methods=['POST'])
def process_data():
    try:
        data = request.json
        weight = int(data.get('weight'))
        height = int(data.get('height'))
        age = int(data.get('age'))

        if age < 6 or age > 23:
            return jsonify({'error': 'This system only works for kids aged 6-23 months old.'}), 400

        # Create an instance of the FeedingExpert class
        expert = FeedingExpert()

        # Get recommendations from the expert system
        recommendations = expert.get_recommendations(age)

        # Include recommendations from the expert system
        feedback += "<br><b>Expert System Recommendations:</b><br>"
        feedback += recommendations

        return jsonify({'recommendations': recommendations, 'feedback': feedback})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
