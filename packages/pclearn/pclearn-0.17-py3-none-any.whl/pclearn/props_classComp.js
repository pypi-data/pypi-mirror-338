//Parent.js
import React, { Component } from "react";
import Child from './child.js';
class Parent extends Component {
    render() {
        return (
            <div>
                <h1>Using Class Component: Parent Component</h1>
                <Child attributeName="abc" />
            </div>
        );
    }
}
export default Parent;















//Child.js
import React, { Component } from "react";
class Child extends Component {
    render() {
        return (
            <div>
                <h2>This is Child Component</h2>
                <h3>From Child Component: {this.props.attributeName}</h3>
            </div>
        );
    }
}
export default Child;



//App.js
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
