//winresize.js
import React, { useEffect, useState } from 'react'
export default function Q2() {
    const [winsize,setwinsize]=useState({})
    useEffect(()=>{
        const handlewin=()=>{
            setwinsize({"width":window.innerWidth,"height":window.innerHeight})
        }
        window.addEventListener("resize",handlewin)
        return()=>(
            window.removeEventListener("resize",handlewin)
        )
    },[])
  return (
    <div>
      <h2>Width : {winsize.width}</h2>
      <h2>Height : {winsize.height}</h2>
    </div>
  )
}














//app.js
import React from 'react';
import './App.css';
import Q2 from './winresize'; 
function App() {
    return (
        <div className="App">
            <Q2 />
        </div>
    );
}

export default App;