const mongoose = require("mongoose");
async function connectDB() {
  try {
    await mongoose.connect("mongodb://localhost:27017", {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log("Connected to MongoDB Compass successfully!");
  } catch (err) {
    console.error("Error connecting to MongoDB Compass:", err);
  }
}
connectDB();
