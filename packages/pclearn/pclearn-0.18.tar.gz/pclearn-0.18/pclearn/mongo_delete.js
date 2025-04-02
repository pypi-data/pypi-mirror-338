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
    const id = parseInt(await new Promise(resolve => rl.question("Enter User ID to delete: ", resolve)));
    const existingUser  = await User.findOne({ id });
    if (!existingUser ) {
      console.error("Error: User ID not found.");
    } else {
      await User.deleteOne({ id });
      console.log(`User  with ID ${id} deleted successfully!`);
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