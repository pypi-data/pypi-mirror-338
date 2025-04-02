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
    const id = parseInt(await new Promise(resolve => rl.question("Enter User ID to update: ", resolve)));
    const existingUser  = await User.findOne({ id });
    if (!existingUser ) {
      console.error("Error: User ID not found.");
    } else {
      const name = await new Promise(resolve => rl.question("Enter new Name: ", resolve));
      const age = parseInt(await new Promise(resolve => rl.question("Enter new Age: ", resolve)));
      await User.updateOne({ id }, { $set: { name, age } });
      console.log(`User  with ID ${id} updated successfully!`);
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