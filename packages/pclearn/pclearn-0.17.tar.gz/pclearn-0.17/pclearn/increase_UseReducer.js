//Increment.js
import { useReducer } from "react";
function Reducer() {
    const [state, dispatch] = useReducer(reducer, { age: 0 });
    function reducer(state, action) {
        switch (action.type) {
            case 'increment':
                return { age: state.age + 1 };
            case 'decrement':
                return { age: state.age - 1 };
            case 'reset':
                return { age: 0 };
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
            <h1>Incrementing Age using useReducer</h1>
            <h2>Age: {state.age}</h2>
            <button onClick={Increment}>Increment Age</button>
            <button onClick={Decrement}>Decrement Age</button>
            <button onClick={Reset}>Reset Age</button>
        </div>
    );
}
export default Reducer;













//App.js
import Reducer from './Increment.js';
function App() {
 return (
 <div className="App">
 <Reducer/>
 </div>
 );
}
export default App;