import express from "express";
const jwt = require('jsonwebtoken');
const users = require('../controllers/User');
const dotenv = require("dotenv");
dotenv.config();

module.exports = async (req:express.Request, res:express.Response, next) => {
  try {
    const token = req.headers.token;
    const refreshToken = req.headers.token;
    const decodedRefreshToken = jwt.verify(refreshToken, process.env.JWT_SECRET);
    const decodedToken = jwt.verify(refreshToken, process.env.JWT_SECRET);

    
    const userId = decodedRefreshToken._id;
    
    if (!await users.verifyUserId(userId)) {
        console.log('auth failed')
        throw 'Invalid user ID';
    } else {
        // if the refresh token is correct, refresh the regular token for an hour.
        res.setHeader('token', jwt.sign({_id: userId}, process.env.JWT_SECRET, {expiresIn: "1h"}))
        next();
    }
  } catch {
    res.json({
      status: 'ko',
      error: "Unauthorized request",
    });
  }
};
