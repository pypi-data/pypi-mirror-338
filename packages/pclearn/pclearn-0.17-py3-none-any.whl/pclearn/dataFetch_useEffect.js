//datafetch
import { useEffect,useState } from "react";
export default function Q1(){
    const [posts, setposts] = useState([]);
    useEffect(()=>{
        const fetchData=async ()=>{
            const res= await fetch('https://jsonplaceholder.typicode.com/posts');
            const data=await res.json();
            setposts(data);
        }
        fetchData();
    },[])
    return(
        <div>
            {posts.map((post)=>(
                <div key={post.id}>
                    <h1>{post.id}</h1>
                    <p>Title: {post.title}</p>
                    <p>Body: {post.body}</p> 
                </div>
            ))}
        </div>
    )
}
















//Appp.js
import React from 'react';
import './App.css';
import Q1 from './datafetch'; 
function App() {
    return (
        <div className="App">
            <Q1 />
        </div>
    );
}
export default App;