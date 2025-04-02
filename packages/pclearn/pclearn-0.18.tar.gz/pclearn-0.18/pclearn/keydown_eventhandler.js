//keydown.js
import React, { useState } from "react";
export default function Q2() {
  const [value, setValue] = useState("");
  const handleInputChange = (e) => {
    setValue(e.target.value); 
  };
  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      console.log(`Input Value is: ${value}`); 
    }
  };
  return (
    <div>
      <input
        type="text"
        onChange={handleInputChange} 
        onKeyDown={handleKeyDown} 
      />
    </div>
  );
}


















//app.js
import React from 'react';
import './App.css';
import Q2 from './keydown'; 
function App() {
    return (
        <div className="App">
            <Q2 />
        </div>
    );
}

export default App;