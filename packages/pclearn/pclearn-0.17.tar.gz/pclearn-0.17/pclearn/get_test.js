const express= require('express');
const fs= require('fs');
const app=express();
const port= 3000;
const users=JSON.parse(fs.readFileSync('users.json','utf-8'));
app.get('/users',(req,res)=>{
 res.send(users);
})
app.get('/users/:id',(req,res)=>{
 const user=parseInt(req.params.id);
 const userId=users.find((u)=>u.id===user);
 if(userId){
 res.json(userId);
 }
 else{
 res.send(`User with ${userId} is not found`);
 }
})
app.listen(port,()=>{
 console.log(`App is listening on port ${port}`);
})
