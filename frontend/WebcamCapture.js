import React, { useRef, useState } from 'react';
import Webcam from 'react-webcam';
import { sendImageForAuth } from './api';

const WebcamCapture = () => {
  const webcamRef = useRef(null);
  const [result, setResult] = useState('');

  const capture = async () => {
    const imageSrc = webcamRef.current.getScreenshot().split(',')[1];
    const response = await sendImageForAuth(imageSrc);
    if (response.success) {
      setResult(`Welcome, ${response.user}`);
    } else {
      setResult(`Authentication failed: ${response.error}`);
    }
  };

  return (
    <div>
      <Webcam
        audio={false}
        height={320}
        ref={webcamRef}
        screenshotFormat="image/jpeg"
        width={480}
      />
      <button className="btn btn-primary mt-2" onClick={capture}>Authenticate</button>
      <p>{result}</p>
    </div>
  );
};

export default WebcamCapture;
