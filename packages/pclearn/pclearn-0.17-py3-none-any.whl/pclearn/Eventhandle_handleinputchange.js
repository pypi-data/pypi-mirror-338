//Event.js
import React, { useState } from 'react';
export default function Q1() {
    const [value, setValue] = useState('');
    const handleSubmit = (event) => {
        event.preventDefault(); 
        console.log(`Form submitted with input value: ${value}`);
    };
    const handleInputChange = (event) => {
        setValue(event.target.value); 
    };
    return (
        <div>
            <form onSubmit={handleSubmit}>
                <h1>Value: {value}</h1>
                <input type='text' onChange={handleInputChange} />
                <button type='submit'>Submit</button>
            </form>
        </div>
    );
}



















//app.js
import React from 'react';
import './App.css';
import Q1 from './Event'; 
function App() {
    return (
        <div className="App">
            <Q1 />
        </div>
    );
}
export default App;