//array.js
import React, { useState } from 'react';
export default function Q3() {
    const [value, setValue] = useState('');
    const [array, setArray] = useState([]);
    const handleArray = () => {
        if (value.trim() !== '') {
            setArray([...array, value]);
            setValue('');
        }
    };
    const handleInput = (e) => {
        setValue(e.target.value);
    };
    //for delete elemnet 
    const handleDelete = (index) => {
        setArray(array.filter((_, i) => i !== index));
    };
    return (
        <div>
            <input type='text' value={value} onChange={handleInput} />
            <button onClick={handleArray}>Add</button>
            <div>
                <h2>Elements of array:</h2>
                <ul>
                    {array.map((item, index) => (
                        <li key={index}>
                            {item} 
                            <button onClick={() => handleDelete(index)}>Delete</button> {/* remove the button tag if delete element is not required */ }
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
}












//App.js
import React from 'react';
import './App.css';
import Q3 from './array'; 
function App() {
    return (
        <div className="App">
            <Q3 />
        </div>
    );
}

export default App;