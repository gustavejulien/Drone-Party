# Drone-Party

End of year project for the Pre-MSC pro course.
The objective of this project is to provide a drone rich in functionality. This drone will offer many means of control and many features. 
In means of control we will find :
- Voice recognition
- Qt client and electron client
- A web client 
The main features will be the following: 
- "Doggie" mode, the drone will follow the user
- "Patrol" mode, the drone will patrol and at the meeting of some faces emit a sound. 
- "Control" mode, this mode lets the user control the drone from one of the clients.  


## Usage

### Web client

Enter the command

```bash
npm install
```

Very important:
Replace this line:

```js
console.error("Unknown button " + buttonName);
```

by this one:

```js
return;
```

in the file located at

```
client_web/drone-front/node_modules/react-gamepad/lib/Gamepad.js
```
