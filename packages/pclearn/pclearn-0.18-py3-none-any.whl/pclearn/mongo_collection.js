const mongoose = require("mongoose");
async function main() {
  try {
    await mongoose.connect("mongodb://localhost:27017", {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log("Connected to MongoDB Compass successfully!");
    const userSchema = new mongoose.Schema({
      id:Number,
      name: String,
      age: Number,
    });
    const User = mongoose.model("User", userSchema);
    console.log("Collection 'Users' created successfully!");
    mongoose.connection.close();
  } catch (err) {
    console.error("Error:", err);
  }
}
main();
