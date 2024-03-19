import React, { useState } from 'react';
import './App.css';

function App() {
  const [weight, setWeight] = useState('');
  const [height, setHeight] = useState('');
  const [age, setAge] = useState('');
  const [recommendations, setRecommendations] = useState('');
  const [feedback, setFeedback] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async () => {

    // Input validation
    if (!weight || !height || !age) {
      setError('Please enter values for weight, height, and age.');
      return;
    }
    if (isNaN(weight) || isNaN(height) || isNaN(age)) {
      setError('Please enter numeric values for weight, height, and age.');
      return;
    }
    const ageInt = parseInt(age, 10);
    if (ageInt < 6 || ageInt > 23) {
      setError('This system only works for kids aged 6-23 months old.');
      return;
    }
    // Clear previous error message
    setError('');


    // POST data to backend
    try {
      const response = await fetch('http://localhost:5000/process-data', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ weight, height, age })
      });
  
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Failed to process data');
      }
  
      const responseData = await response.json();
      setRecommendations(responseData.recommendations);
      setFeedback(responseData.feedback);
    } catch (error) {
      console.error('Error processing data:', error.message);
      // display error message to the user)
    }
  };

  return (
    <div className="container">
      <h1>Child Weaning Recommendations System</h1>
      <div className="input-group">
        <label>Weight (kg):</label>
        <input type="number" value={weight} onChange={(e) => setWeight(e.target.value)} />
      </div>
      <div className="input-group">
        <label>Height (cm):</label>
        <input type="number" value={height} onChange={(e) => setHeight(e.target.value)} />
      </div>
      <div className="input-group">
        <label>Age (months):</label>
        <input type="number" value={age} onChange={(e) => setAge(e.target.value)} />
      </div>
      <button onClick={handleSubmit}>Submit</button>
      <div className="output">
        <h2>Food Recommendations:</h2>
        <p>{recommendations}</p>
        <h2>Nutrition Feedback:</h2>
        <p>{feedback}</p>
      </div>
    </div>
  );
}

export default App;
