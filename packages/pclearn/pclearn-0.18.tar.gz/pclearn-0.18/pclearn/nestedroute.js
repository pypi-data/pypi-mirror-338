//home.js
import React from 'react';
import { Link } from "react-router-dom";
function Home() {
  return (
    <div>
      <h1>This is the home page</h1>
      <Link to="/about">Click to view our about page</Link><br />
      <Link to="/contact">Click to view our contact page</Link>
    </div>
  );
}
export default Home;

















//contact.js
import React from 'react';
import { Link, Outlet } from 'react-router-dom';
function ContactHome(){
    return (
        <div>
            <h1>This is the contact page</h1>
            <Link to="/">Go back to home</Link>
                      <nav>
                <ul>
                    <li>
                        <Link to="add">Add Contact</Link>
                    </li>
                    <li>
                        <Link to="display">Display Contacts</Link>
                    </li>
                </ul>
            </nav>
            <Outlet /> 
        </div>
    );
}
function Contact() {
  return (
        <ContactHome/>
  );
}
export default Contact;














//about.js
import React from 'react';
import { Link } from 'react-router-dom';
function About() {
  return (
    <div>
      <h1>This is the about page.</h1>
      <Link to="/">Go back to home</Link>
    </div>
  );
}
export default About;





//add.js
import React from 'react';
function Add() {
  return (
    <div>
      <h2>Add Contact</h2>
    </div>
  );
}
export default Add;




//display.js
import React from 'react';
function Display() {
    return (
      <div>
        <h2>Display Contacts</h2>
      </div>
    );
  }
  export default Display;











//index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter } from 'react-router-dom';
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter> 
    <App />
    </BrowserRouter>
  </React.StrictMode>
);






//app.js
import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './home';
import About from './about';
import Contact from './contact';
import Add from './add';
import Display from './display';
function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/about" element={<About />} />
      <Route path="/contact" element={<Contact />}>
        <Route path="add" element={<Add />} />
        <Route path="display" element={<Display />} />
      </Route>
    </Routes>
  );
}
export default App;
