//addremove.js
import React, { useState } from "react";
export default function Q4() {
  const [value, setValue] = useState("");
  const [list, setList] = useState([]);
  const handleInput = (e) => setValue(e.target.value);
  const updateList = (action, index) => {
    const updatedList = [...list];
    if (action === "add" && value.trim()) updatedList.push(value);
    if (action === "addAfter" && value.trim()) updatedList.splice(index + 1, 0, value);
    if (action === "remove") updatedList.splice(index, 1);
    setList(updatedList);
    setValue("");
  };
  return (
    <div style={{ padding: "20px" }}>
      <h2>User Management</h2>
      <div style={{ marginBottom: "20px" }}>
        <input
          type="text"
          value={value}
          onChange={handleInput}
          placeholder="Enter user name"
          style={{ marginRight: "10px", padding: "5px" }}
        />
        <button onClick={() => updateList("add")} disabled={!value.trim()}>Add</button>
      </div>
      {list.map((item, index) => (
        <div key={index} style={{ display: "flex", alignItems: "center", marginBottom: "10px" }}>
          <h3 style={{ marginRight: "10px" }}>{item}</h3>
          <button onClick={() => updateList("remove", index)} style={{ marginRight: "10px" }}>
            Remove
          </button>
          <input
            type="text"
            value={value}
            onChange={handleInput}
            placeholder="Add after this user"
            style={{ marginRight: "10px", padding: "5px" }}
          />
          <button onClick={() => updateList("addAfter", index)} disabled={!value.trim()}>
            Add After
          </button>
        </div>
      ))}
      {list.length === 0 && <p>No users added yet.</p>}
    </div>
  );
}





















//App.js
import React from 'react';
import './App.css';
import Q4 from './addremove'; 
function App() {
    return (
        <div className="App">
            <Q4 />
        </div>
    );
}
export default App;