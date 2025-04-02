//countdown.js
import React, { useEffect, useState } from 'react';
export default function Q1() {
    const [time, setTime] = useState(20)
    const [value,setvalue]=useState('')
    useEffect(() => {
        const id = setInterval(() => {
            setTime(prevTime => prevTime - 1)
        }, 1000);
        if (time === 0) {
            setvalue("Time's Up")
            clearInterval(id);
        }
        return () => clearInterval(id)
    }, [time])
    return (
        <div>
            <h2>Time remain's : {time}</h2>
            <h1>{value}</h1>
        </div>
    );
}















//App.js
countdown
import React from 'react';
import './App.css';
import Q1 from './countdown'; 
function App() {
    return (
        <div className="App">
            <Q1 />
        </div>
    );
}

export default App;