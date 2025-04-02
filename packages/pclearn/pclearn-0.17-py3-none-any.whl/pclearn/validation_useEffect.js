//validation.js
import { useEffect, useState } from "react";
export default function Q2() {
    const [inpVal, setinpVal] = useState("");
    const [isValid, setisValid] = useState(true);
    const [errorMessage, setErrorMessage] = useState("");
    useEffect(() => {
        const isValidInp = inpVal.length >= 5 && /[A-Z]/.test(inpVal) && /[0-9]/.test(inpVal);
        setisValid(isValidInp);
        setErrorMessage(isValidInp ? "" : "Input must be at least 5 characters long and contain at least one uppercase letter and one number.");
    }, [inpVal]);
    const handleSubmit = (event) => {
        event.preventDefault();
        if (isValid) {
            console.log("Form submitted successfully with Input value: ", inpVal);
        } else {
            alert("Incorrect input value. Value must meet the specified criteria.");
        }
        setinpVal("");
    };
    const handleInput = (event) => {
        setinpVal(event.target.value);
    };
    return (
        <div>
            <form onSubmit={handleSubmit}>
                <h2>Input Validation using useEffect</h2>
                <label>Enter some text: </label>
                <input type="text" value={inpVal} onChange={handleInput} />
                <br />
                {!isValid && <p style={{ color: "red" }}>{errorMessage}</p>}
                <button type="submit">Submit</button>
            </form>
        </div>
    );
}


























//App.js
import React from 'react';
import './App.css';
import Q2 from './validation'; 
function App() {
    return (
        <div className="App">
            <Q2 />
        </div>
    );
}

export default App;