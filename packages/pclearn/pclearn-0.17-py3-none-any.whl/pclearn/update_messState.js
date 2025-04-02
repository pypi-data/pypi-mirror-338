//Message.js
import React, { Component } from "react";
class Message extends Component {
    constructor() {
        super();
        this.state = {
            message: "Hello "
        };
        this.changeMsg = this.changeMsg.bind(this);
    }
    changeMsg() {
        this.setState({
            message: "Hi"
        });
    }
    render() {
        return (
            <div>
                <h1>{this.state.message}</h1>
                <button onClick={this.changeMsg}>Click me</button>
            </div>
        );
    }
}
export default Message;

















//APP.js
import './App.css'; 
import Message from './Message.js'; 

function App() {
    return (
        <div className="App">
            <Message /> 
        </div>
    );
}

export default App; 
