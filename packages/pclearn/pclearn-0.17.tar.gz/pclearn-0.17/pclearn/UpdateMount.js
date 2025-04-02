//update.js
import React, { Component } from 'react';
class Update extends Component {
  constructor(props) {
    super(props);
    this.state = {
      State: props.s};
  }
  componentDidUpdate(prevProps) {
    if (this.props.s !== prevProps.s) {
      this.setState({
        State: this.props.s
      });
    }
    console.log("component updated")
  }
  render() {
    return (
      <div>
        {this.state.State}
      </div>
    );
  }
}
export default Update;














//App.js
import React, { useState } from 'react';
import './App.css';
import Update from './update'; 
function App() {
    const [value, setValue] = useState("hello");
    return (
        <div className="App">
            <Update s={value} />
            <button onClick={() => setValue("Welcome To Mcc")}>Update Value</button>
        </div>
    );
}
export default App;