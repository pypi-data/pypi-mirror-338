//Counter.js
import React, { useReducer } from "react";
function Reducer() {
    const [state, dispatch] = useReducer(reducer, { count: 0 });

    function reducer(state, action) {
        switch (action.type) {
            case 'increment':
                return { count: state.count + 1 };
            case 'decrement':
                return { count: state.count - 1 };
            case 'reset':
                return { count: 0 };
            default:
                throw new Error('Invalid action type');
        }
    }

    function Increment() {
        dispatch({ type: 'increment' });
    }
    function Decrement() {
        dispatch({ type: 'decrement' });
    }
    function Reset() {
        dispatch({ type: 'reset' });
    }
    return (
        <div>
            <h1>Incrementing Counter using useReducer</h1>
            <h2>Count: {state.count}</h2>
            <button onClick={Increment}>Increment</button>
            <button onClick={Decrement}>Decrement</button>
            <button onClick={Reset}>Reset</button>
        </div>
    );
}
export default Reducer;




















//App.js
import Reducer from './Counter.js';
function App() {
 return (
 <div className="App">
 <Reducer/>
 </div>
 );
}
export default App;