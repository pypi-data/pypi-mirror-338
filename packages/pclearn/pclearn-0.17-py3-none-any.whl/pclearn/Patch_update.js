const express = require('express');
const fs = require('fs');
const app = express();
const port = 3000;
app.use(express.json());
let users = JSON.parse(fs.readFileSync('users.json', 'utf-8'));
app.get('/users', (req, res) => res.json(users));
app.get('/users/:id', (req, res) => {
    const user = users.find(u => u.id === +req.params.id);
    res.json(user || { message: "User  not found" }).status(user ? 200 : 404);
});
app.patch('/users/:id', (req, res) => {
    const userId = +req.params.id;
    const newName = req.query.name || req.body.name;
    if (!newName) return res.status(400).json({ message: "Name is required" });
    const user = users.find(u => u.id === userId);
    if (!user) return res.status(404).json({ message: `User  with id ${userId} not found` });
    user.name = newName;
    fs.writeFileSync('users.json', JSON.stringify(users, null, 2));
    res.json({ message: `User  with id ${userId} updated successfully`, user });
});
app.listen(port, () => console.log(`App is listening on port ${port}`));