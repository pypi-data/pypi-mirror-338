//Parent.js
import React, { useRef } from 'react';
import Child from './Child';
const Parent = () => {
  const childRef = useRef();
  const handleClick = () => {
    if (childRef.current) {
      childRef.current.showMessage(); 
    }
  };
  return (
    <div>
      <h1>Parent Component</h1>
      <button onClick={handleClick}>Call Child Function</button>
      <Prac7Q3Child ref={childRef} />
    </div>
  );
};
export default Parent;












//Child.js
import React, { forwardRef, useImperativeHandle } from 'react';
const Child = forwardRef((props, ref) => {
  const showMessage = () => {
    console.log('Function called from child component!');
  };
  useImperativeHandle(ref, () => ({
    showMessage, 
  }));
  return <div>hello</div>;
});
export default Child;






//App.js
import React from 'react';
import './App.css';
import Parent from './Parent'; 
function App() {
    return (
        <div className="App">
            <Parent />
        </div>
    );
}
export default App;