//Counter.js
import React from "react";
import {Component} from "react";
class Counter extends Component{
    constructor(){
        super()
        this.state={
            ctr:0
        }
    }
    render(){
        return(
            <div>
                <h1>Creating Counter  using React</h1>
                <h2></h2>
                <h1>Counter: {this.state.ctr}</h1>
                <button onClick={()=>this.CtrInc()}>Click me</button>
                
            </div>
        );
    }
    CtrInc(){
        this.setState({
            ctr:this.state.ctr+1
        }
        )
    }
}
export default Counter;


















//App.js
import './App.css';
import Counter from './Counter.js';
function App() {
 return (
 <div className="App">
 <Counter/>
 </div>
 );
}
export default App;