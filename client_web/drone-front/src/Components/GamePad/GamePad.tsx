import React from "react";
import Gamepad from "react-gamepad";
import { AxisStates, ButtonsStates } from "../../Models/types";

type Props = {
  onConnectChange?: (isConnected: boolean) => void;
  onButtonChange?: (buttons: ButtonsStates) => void;
  onAxisChange?: (axis: AxisStates) => void;
};

const GamePad = ({ onConnectChange, onButtonChange, onAxisChange }: Props) => {
  const connectHandler = (gamepadIndex: Number) => {
    console.log(`Gamepad ${gamepadIndex} connected !`);
    onConnectChange && onConnectChange(true);
  };

  const disconnectHandler = (gamepadIndex: Number) => {
    console.log(`Gamepad ${gamepadIndex} disconnected !`);
    onConnectChange && onConnectChange(false);
  };

  const buttonChangeHandler = (buttonName: string, down: boolean) => {
    console.log(buttonName, down);
    onButtonChange &&
      onButtonChange({ buttonName: buttonName, isPressed: down });
  };

  const axisChangeHandler = (
    axisName: string,
    value: number,
    previousValue: number
  ) => {
    onAxisChange && onAxisChange({ axisName: axisName, value: value });
  };

  // const buttonDownHandler = (buttonName: String) => {
  //   console.log(buttonName, "down");
  // };

  // const buttonUpHandler = (buttonName: String) => {
  //   console.log(buttonName, "up");
  // };
  return (
    <>
      <Gamepad
        onConnect={connectHandler}
        onDisconnect={disconnectHandler}
        onButtonChange={buttonChangeHandler}
        onAxisChange={axisChangeHandler}
      >
        <p></p>
      </Gamepad>
    </>
  );
};

export default GamePad;
