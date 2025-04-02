const mongoose = require("mongoose");
const User = require("./Myschema");
async function main() {
  try {
    await mongoose.connect("mongodb://localhost:27017", {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log("Connected to MongoDB Compass successfully!");
    const users = await User.find();
    if (users.length) {
      console.log("Users in the database:");
      console.table(users.map(({ id, name, age }) => ({ ID: id, Name: name, Age: age })));
    } else {
      console.log("No users found in the database.");
    }
  } catch (err) {
    console.error("Error:", err);
  } finally {
    mongoose.connection.close();
  }
}
main();

















//Myschema

const mongoose = require("mongoose");
const userSchema = new mongoose.Schema({
  id: { type: Number, unique: true },
  name: String,
  age: Number,
});
const User = mongoose.model("User", userSchema);
module.exports = User;