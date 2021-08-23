const MongoClient = require('mongodb').MongoClient;
import dotenv from 'dotenv';
import mongoose from 'mongoose';
dotenv.config();
const uri: string = process.env.MONGO_URI;

const connectToDatabase = async() => {
  try{
    await mongoose.connect(uri, { useCreateIndex:true, useFindAndModify:true, useNewUrlParser: true, useUnifiedTopology: true });
    console.log('Connection to the database established');
  }catch(error){
    console.log(error);
    process.exit(1);
  }
}

module.exports = connectToDatabase;