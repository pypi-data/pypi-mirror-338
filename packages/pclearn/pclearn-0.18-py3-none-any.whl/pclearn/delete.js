const express = require("express");
const fs = require("fs");
const app = express();
const PORT = 3000;
app.use(express.json());
let users = JSON.parse(fs.readFileSync("users.json", "utf8"));
app.get("/users", (req, res) => res.json(users));
app.get("/users/:id", (req, res) => {
    const user = users.find(u => u.id === +req.params.id);
    res.status(user ? 200 : 404).json(user || { message: "User  not found" });
});
app.delete('/users/:id', (req, res) => {
    const id = +req.params.id;
    users = users.filter(user => user.id !== id);
    fs.writeFileSync('users.json', JSON.stringify(users, null, 2));
    res.json({ message: `User  with id ${id} deleted successfully` });
});
app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));