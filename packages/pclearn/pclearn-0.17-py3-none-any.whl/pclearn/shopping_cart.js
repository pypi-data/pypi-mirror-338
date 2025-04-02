//shopping.js
import React, { createContext, useState, useContext } from 'react';
const CartContext = createContext();
export function CartProvider() {
  const [cart, setCart] = useState([]);
  const addToCart = (item) => {
    setCart([...cart, item]);
  };
  const removeFromCart = (index) => {
    setCart(cart.filter((_, i) => i !== index));
  };
  return (
    <CartContext.Provider value={{ cart, addToCart, removeFromCart }}>
      <div className="app-container">
        <Cart />
        <ProductList />
      </div>
    </CartContext.Provider>
  );
}
function Cart() {
  const { cart, removeFromCart } = useContext(CartContext);
  return (
    <div className="cart">
      <h2>Shopping Cart</h2>
      {cart.length === 0 ? (
        <p>Your cart is empty</p>
      ) : (
        <ul>
          {cart.map((item, index) => (
            <li key={index}>
              {item.name} - Ruppes{item.price}
              <button onClick={() => removeFromCart(index)}>Remove</button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
// ProductList component
function ProductList() {
  const { addToCart } = useContext(CartContext);
  const products = [
    { id: 1, name: 'Smartwatch', price: 1500 },
    { id: 2, name: 'Smartphone', price: 25000 },
    { id: 3, name: 'Headphones', price: 1999 },
    { id: 4, name: 'Laptop', price: 45000},
  ];
  return (
    <div className="product-list">
      <h2>Products</h2>
      <ul>
        {products.map((product) => (
          <li key={product.id}>
            {product.name} - Ruppes{product.price}
            <button onClick={() => addToCart(product)}>Add to Cart</button>
          </li>
        ))}
      </ul>
    </div>
  );
}


























//App.js
import React from "react";
import "./App.css";
import { CartProvider } from "./shopping"
function App() {
return (
<div className="app">
<h1>Shopping Cart </h1>
<CartProvider />
</div>
);
}
export default App;