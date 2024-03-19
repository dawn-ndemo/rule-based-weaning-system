import React, { useState } from 'react';
import './App.css';

function App() {
  const [weight, setWeight] = useState('');
  const [height, setHeight] = useState('');
  const [age, setAge] = useState('');
  const [recommendations, setRecommendations] = useState('');
  const [feedback, setFeedback] = useState('');

  const handleSubmit = () => {
    // Validate input data
    if (age < 6 || age > 23) {
      alert('This system only works for kids aged 6-23 months old.');
      return;
    }

    // To insert here an API request to the Python backend to pass the weight, height, and age data
    // Example:
    // axios.post('/process-data', { weight, height, age })
    //   .then(response => {
    //     setRecommendations(response.data.recommendations);
    //     setFeedback(response.data.feedback);
    //   })
    //   .catch(error => console.error('Error processing data:', error));

    // to replace this after doing the API
    setRecommendations('Sample food recommendations');
    setFeedback('Sample nutrition feedback');
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
