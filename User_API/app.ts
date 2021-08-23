import express from 'express';
import * as userControllers from './controllers/User';
import auth from './middlewares/jwt'
const app = express();
const connectTodatabase = require('./configuration/connectToDatabase');
const cors = require('cors');

connectTodatabase();
app.use(express.urlencoded({extended: true}));
app.use(express.json())

app.get('/', (req, res) => {
    res.send('Hello from express and typescript');
})

app.post('/user', userControllers.createUser);
app.get('/user', auth, userControllers.getUser);
app.put('/user', auth, userControllers.updateUser);
app.delete('/user', auth, userControllers.deleteUser);
app.post('/connect', userControllers.login);
app.get('/refreshtoken', userControllers.refreshToken);
app.get('/verifytoken', userControllers.verifyToken);

export {app};