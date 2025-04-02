//FormWithRef.js
import React, { useRef } from 'react';
export default function FormWithRef() {
  const usernameRef = useRef();
  const emailRef = useRef();
  const handleSubmit = () => {
    console.log(
      `Submitted Data: \nUsername: ${usernameRef.current.value}, Email: ${emailRef.current.value}`
    );
  };
  return (
    <div>
      <input type="text" placeholder="Enter Name..." ref={usernameRef} />
      <input type="email" placeholder="Enter Email..." ref={emailRef} />
      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
}


















//App.js
import React from 'react';
import './App.css';
import FormWithRef from './FormWithRef'; 
function App() {
    return (
        <div className="App">
            <FormWithRef />
        </div>
    );
}
export default App;