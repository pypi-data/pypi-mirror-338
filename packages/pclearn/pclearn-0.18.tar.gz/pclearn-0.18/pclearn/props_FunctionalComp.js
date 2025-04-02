//Parent.js
import React from "react";
import Child from './child.js'
function Parent(){
    return(
        <div>
            <h1>Using Functional Component: Parent Component</h1>
            <Child attributeName="abc"/>
        </div>
    )
}
export default Parent;






















//child.js
import React from "react"
function Child(props){
    return(
        <div>
            <h2>This is Child Component</h2>
            <h3>From Child Component: {props.attributeName}</h3>
        </div>
    )
}
export default Child;




//App.js

App.js
import './App.css';
import Parent from './Parent.js';
function App() {
 return (
 <div className="App">
 <Parent/>
 </div>
 );
}
export default App;
