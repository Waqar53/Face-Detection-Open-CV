import React from 'react';
import WebcamCapture from './WebcamCapture';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <div className="container mt-5">
      <h2>Face Authentication</h2>
      <WebcamCapture />
    </div>
  );
}

export default App;
