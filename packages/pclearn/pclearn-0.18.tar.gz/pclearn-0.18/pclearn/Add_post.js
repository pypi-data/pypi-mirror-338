const express = require("express");
const fs = require("fs");
const app = express();
const PORT = 3000;
app.use(express.json());
const users = JSON.parse(fs.readFileSync("users.json", "utf8"));
app.get("/users", (req, res) => res.json(users));
app.get("/users/:id", (req, res) => {
    const user = users.find(u => u.id === +req.params.id);
    res.status(user ? 200 : 404).json(user || { message: "User  not found" });
});
app.post('/users/:id', (req, res) => {
    const userId = +req.params.id;
    const { name, age } = req.body;
    if (!name || !age) return res.status(400).json({ message: "Name and age are required" });
    if (users.find(u => u.id === userId)) return res.status(400).json({ message: `User  with ID ${userId} already exists` });
    const newUser  = { id: userId, name, age };
    users.push(newUser );
    fs.writeFileSync("users.json", JSON.stringify(users, null, 2), "utf8");
    res.status(201).json({ message: "User  added successfully", user: newUser  });
});
app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));