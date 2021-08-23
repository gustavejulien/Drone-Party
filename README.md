# Final Project

A project where you can control a drone, take pictures from it and access multiple modes with web client and software client.

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
T-YEP-600-PAR-6-1-finalproject-louis-auguste.dumas/client_web/drone-front/node_modules/react-gamepad/lib/Gamepad.js
```
