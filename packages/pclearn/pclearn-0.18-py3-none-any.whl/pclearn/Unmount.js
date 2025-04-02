//Unmount.js
import React, { Component } from 'react'
export class Unmount extends Component {
    constructor(){
        super();
        this.state={show:false};
    }
  render() {
    return (
      <div>
        {this.state.show?<Child/>:<h2>Hello</h2>}
        <button onClick={()=>this.setState({show:!this.state.show})}>Click me</button>
      </div>
    )
  }
}
class Child extends Component{
    componentWillUnmount(){
        alert("Component unmounted")
    }
    render(){
        return(
            <div>
                <h1>This is child component</h1>
            </div>
        )
    }
}
export default Unmount
































//App.js
import React from 'react';
import './App.css';
import Unmount from './Unmount'; // Adjust the path as necessary
function App() {
    return (
        <div className="App">
            <Unmount />
        </div>
    );
}
export default App;