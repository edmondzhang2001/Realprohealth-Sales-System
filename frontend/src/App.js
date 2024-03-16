import React from 'react';
import logo from './logo.svg';
import './App.css';
import SalesForm from './salesForm';

function App() {
  const handleSubmit = async (formData) => {
    try {
      const response = await fetch('http://127.0.0.1:5000/api/sales', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      });
      if (response.ok) {
        console.log('Sale created successfully!');
        // Clear form fields or show success message
      } else {
        console.error('Failed to create sale:', await response.text());
        // Show error message to the user
      }
    } catch (error) {
      console.error('Error creating sale:', error.message);
      // Handle network errors
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <SalesForm onSubmit={handleSubmit} />
      </header>
    </div>
  );
}

export default App;
