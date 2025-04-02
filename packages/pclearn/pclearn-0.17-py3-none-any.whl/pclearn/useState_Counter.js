//Counter.js
import {useState } from 'react';
function Ques1(){
 const [count,setCount]=useState(0);
 return(
 <div>
 <h1>Creating counter using useState in functional component</h1>
 <h3>Sujal More</h3>
 <h1>Counter: {count}</h1>
 <button onClick={()=>setCount(count+1)}>Increase</button>
 <button onClick={()=>setCount(count-1)}>Decrease</button>
 <button onClick={()=>setCount(0)}>Reset</button>
 </div>
 )
}
export default Ques1;

















//App.js
import Ques1 from './Counter.js';
function App() {
 return (
 <div className="App">
 <Ques1/>
 </div>
 );
}
export default App;