//focus.js
import React, { useEffect, useRef } from 'react';
export default function Q1() {
  const inputRef = useRef();
  useEffect(() => {
    inputRef.current.focus();
    console.log('Username input focused');
  }, []);
  return (
    <div>
      <input type="text" placeholder="Enter Name..." ref={inputRef} />
      <input type="email" placeholder="Enter Email..." />
      <button type="submit">Submit</button>
    </div>
  );
}







































//App.js
import React from 'react';
import './App.css';
import Q1 from './focus'; 
function App() {
    return (
        <div className="App">
            <Q1 />
        </div>
    );
}
export default App;