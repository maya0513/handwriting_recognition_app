import React from 'react';
import ImageUpload from './components/ImageUpload';
import './App.css';

const App: React.FC = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Handwritten Digit Recognition</h1>
        <ImageUpload />
      </header>
    </div>
  );
};

export default App;