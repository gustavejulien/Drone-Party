import express from "express";
import dotenv from 'dotenv';
import jwt from 'jsonwebtoken';
import bcrypt from 'bcrypt';
const saltRounds = 10;
dotenv.config();
const ObjectId = require('mongodb').ObjectID
const User = require('../models/UserSch.js');

export async function createUser(req: express.Request, res: express.Response){
    
    let hash:string;
    const username:string = req.body.username;
    const salt = bcrypt.genSaltSync(saltRounds);
    const password:string = bcrypt.hashSync(req.body.password, salt);

    const userExists = await User.findOne({ username: req.body.username })
    if (userExists) {
        return res.json({
            status: 'ko',
            error: "This name is already used."
        });
    }

    const user = new User({
        password:password,
        username:username
    });
    user.save();
    return res.json({ status:'ok', message: "Registration complete."});
}

export async function getUser(req: express.Request, res: express.Response){
    const user = await User.findOne({ username: req.body.username });
    if (!user) {
        return res.json({
            status:'ko',
            error: "Username incorrect."
        });
    }
    return res.json({ status: 'ok', message: user})
}

export async function updateUser(req: express.Request, res: express.Response){
    const { username, password, newUsername, newPassword } = req.body
    
    const user = await User.findOne({ username: username });
    if (!user) {
        return res.json({
            status:'ko',
            error: "Username incorrect."
        });
    }

    const match = await bcrypt.compare(password, user.password);
    if(!match){
        return res.json({
            status:'ko',
            error: "password incorrect."
        });
    } else {
        const update = {};
        if(typeof newUsername === "string"){update['username'] = newUsername}
        const salt = bcrypt.genSaltSync(saltRounds);
        if(typeof newPassword === "string"){update['password'] = bcrypt.hashSync(newPassword, salt)}
        console.log(typeof newUsername, typeof newPassword);
        console.log(newUsername, newPassword, update);
        User.findByIdAndUpdate(user._id, update, function(err, result){
            if(err) res.send(err)
            res.json({status:'ok', message: "User updated."})
        })
    }
}

export async function deleteUser(req: express.Request, res: express.Response){   
    const { username, password } = req.body;
    const user = await User.findOne({ username: req.body.username });

    if (!user) {
        return res.json({
            status: 'ko',
            error: "Username incorrect."
        });
    }

    const match = await bcrypt.compare(password, user.password);
    if(!match){
        return res.json({
            status:'ko',
            error: "password incorrect."
        });
    } else {
        User.findOneAndRemove({username:username}, (err, user) => {
            if(err||!user){
                return res.json({status: 'ko', error:"User credentials incorrect"});
            } else {
                res.json({status: 'ok', message:"User deleted."});
            }
        })
    }
}

export async function login(req: express.Request, res: express.Response){
    const user = await User.findOne({ username: req.body.username });

    if (!user) {
        return res.json({
            status:'ko',
            error: "Username incorrect."
        });
    }

    const match = await bcrypt.compare(req.body.password, user.password);
    if(!match){
        return res.json({
            status:'ko',
            error: "password incorrect."
        });
    } else {
        const refreshToken = jwt.sign({_id: user._id}, process.env.JWT_SECRET);
        const token = jwt.sign({_id: user._id}, process.env.JWT_SECRET, {expiresIn: "1h"});
        return res.json({status:"ok", token:token, refreshtoken:refreshToken});
    }

}

export async function verifyUserId(userId:string){
    
    const user = await User.findById(userId);
    if (!user) {
        return false;
    }else{
        return true;
    }
}

export async function refreshToken(req: express.Request, res: express.Response){
    try {
        const token = req.headers.token;
        const refreshToken = req.headers.token;
        const decodedRefreshToken = jwt.verify(refreshToken, process.env.JWT_SECRET);
        const decodedToken = jwt.verify(refreshToken, process.env.JWT_SECRET);
    
        
        const userId = decodedRefreshToken._id;
        
        if (!await verifyUserId(userId)) {
            console.log('auth failed')
            throw 'Invalid user ID';
        } else {
            // if the refresh token is correct, refresh the regular token for an hour.
            const token = jwt.sign({_id: userId}, process.env.JWT_SECRET, {expiresIn: "1h"});
            res.setHeader('token', token);
            return res.json({status:"ok", token:token, refreshtoken:refreshToken});
        }
      } catch (e) {
        res.json({
            status: 'ko',
            error: "Unauthorized request",
        });
      }
}

export async function refreshToken(req: express.Request, res: express.Response){
    try {
        const token = req.headers.token;
        const refreshToken = req.headers.token;
        const decodedRefreshToken = jwt.verify(refreshToken, process.env.JWT_SECRET);
        const decodedToken = jwt.verify(refreshToken, process.env.JWT_SECRET);
    
        
        const userId = decodedRefreshToken._id;
        
        if (!await verifyUserId(userId)) {
            console.log('auth failed')
            throw 'Invalid user ID';
        } else {
            // if the refresh token is correct, refresh the regular token for an hour.
            const token = jwt.sign({_id: userId}, process.env.JWT_SECRET, {expiresIn: "1h"});
            res.setHeader('token', token);
            return res.json({status:"ok", token:token, refreshtoken:refreshToken});
        }
      } catch (e) {
        res.json({
            status: 'ko',
            error: "Unauthorized request",
        });
      }
}

export async function verifyToken(req: express.Request, res: express.Response){
    try {
        const token = req.headers.token;
        const decodedToken = jwt.verify(refreshToken, process.env.JWT_SECRET);

        if (token === undefined){
            throw new Error('No token given.')
        }
    
        const userId = decodedToken._id;
        
        if (!await verifyUserId(userId)) {
            console.log('auth failed')
            throw 'Invalid user ID';
        } else {
            // if the access token is correct send ok
            return res.json({status:"ok", message:'The access token is valid'});
        }
      } catch (e) {
        res.json({
            status: 'ko',
            error: e,
        });
      }
}
