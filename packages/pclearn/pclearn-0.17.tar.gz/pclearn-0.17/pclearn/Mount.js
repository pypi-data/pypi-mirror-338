//Mount.js
import React, { Component } from 'react'
export default class Mount extends Component {
 constructor(props) {
   super(props)
   this.state={
    text:"Paras"
   }
 }
 componentDidMount(){
    console.log("Component mounted into DOM")
 }
 componentDidUpdate(){
    console.log("Component Update after button click")
 }
  updateName=()=>{
    this.setState({text:"hello"})
  }
  render() {
    return (
      <div>
      <h1>My Name is {this.state.text}</h1>
      <button onClick={this.updateName}>Update the Name</button>
      </div>
    )
  }
}










//app.js
import React from 'react';
import './App.css';
import Mount from './Mount'; 
function App() {
    return (
        <div className="App">
            <Mount />
        </div>
    );
}
export default App;