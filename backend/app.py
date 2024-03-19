# defines my API routes
# defines route for calculating caloric needs using Wt, Ht and age

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate-calories', methods=['POST'])
def calculate_calories():
    data = request.get_json()
    weight_kg = data['weight']
    age_months = data['age']
    height_cm = data['height']

    # Calculate caloric needs (replace with actual calculation)
    # ...

    return jsonify({'calories': calculated_calories})

if __name__ == '__main__':
    app.run(debug=True)
