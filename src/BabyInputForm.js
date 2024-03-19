// src/components/BabyInputForm.js

import React, { useState } from 'react';

const BabyInputForm = () => {
  const [weight, setWeight] = useState('');
  const [height, setHeight] = useState('');
  const [age, setAge] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Makes an API request to Python backend
    try {
      const response = await fetch('/calculate-calories', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ weight, height, age }),
      });

      if (response.ok) {
        const data = await response.json();
        // Handles the calculated calories data (to display it)
        console.log('Calories:', data.calories);
      } else {
        console.error('Error fetching data');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Weight (kg):
        <input
          type="number"
          value={weight}
          onChange={(e) => setWeight(e.target.value)}
        />
      </label>
      <br />
      <label>
        Height (cm):
        <input
          type="number"
          value={height}
          onChange={(e) => setHeight(e.target.value)}
        />
      </label>
      <br />
      <label>
        Age (months):
        <input
          type="number"
          value={age}
          onChange={(e) => setAge(e.target.value)}
        />
      </label>
      <br />
      <button type="submit">Calculate Calories</button>
    </form>
  );
};

export default BabyInputForm;
