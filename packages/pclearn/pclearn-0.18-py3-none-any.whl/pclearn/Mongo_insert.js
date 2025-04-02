const mongoose = require("mongoose");
const readline = require("readline");
const User = require("./Myschema");
async function main() {
  try {
    await mongoose.connect("mongodb://localhost:27017", {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log("Connected to MongoDB Compass successfully!");
    const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
    const askQuestion = (query) => new Promise(resolve => rl.question(query, resolve));
    const id = parseInt(await askQuestion("Enter User ID: "));
    if (await User.findOne({ id })) {
      console.error("Error: ID already exists. Choose a different ID.");
    } else {
      const name = await askQuestion("Enter Name: ");
      const age = parseInt(await askQuestion("Enter Age: "));
      await new User({ id, name, age }).save();
      console.log("User  added successfully!");
    }
    rl.close();
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
