import express from "express";
import * as cors from 'cors';
import dotenv from 'dotenv';
import {app} from './app';

dotenv.config();
const port = process.env.SERVER_PORT;

app.use(function(req, res, next) {  
    res.header('Access-Control-Allow-Origin', "http://localhost:3000");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    res.header("Access-Control-Allow-Credentials", "true")
    next();
});  

app.listen(port, () => console.log('Server started on port '+port));