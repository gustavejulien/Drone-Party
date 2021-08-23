import React, { useEffect, useState } from "react";
import style from "./Controls.module.scss";
import {
  AxisStates,
  ButtonsStates,
  ControllerAxisValues,
  ControllerButtons,
} from "../../Models/types";
import { defaultButtonsStates, defaultAxisStates } from "./initValues";
import { ControlButton, GamePad } from "../";
import {
  up,
  down,
  rotateRight,
  rotateLeft,
  forward,
  backward,
  tiltLeft,
  tiltRight,
  camera,
  controllerActive,
  controllerInactive,
} from "../../Assets/Images";

const Controls = () => {
  //controller
  const [isControllerConnected, setIsControllerConnected] = useState(false);
  const [controllerButtonsStates, setControllerButtonsStates] =
    useState<ControllerButtons>(defaultButtonsStates); //à refacto, pour l'instant on a besoin de connaitre seulement le bouton A
  const [axisStates, setAxisStates] =
    useState<ControllerAxisValues>(defaultAxisStates);
  //

  const handleButtonChange = (buttonState: ButtonsStates) => {
    setControllerButtonsStates((prevState) => ({
      ...prevState,
      [buttonState.buttonName]: buttonState.isPressed,
    }));
  };

  const handleAxisChange = (axisState: AxisStates) => {
    handleStickMove(axisState) &&
      setAxisStates((prevState) => ({
        ...prevState,
        [axisState.axisName]: axisState.value,
      }));
  };

  const handleConnectController = (isConnected: boolean) => {
    setIsControllerConnected(isConnected);
  };

  useEffect(() => {
    controllerButtonsStates.A && handleTakePicture();
  }, [controllerButtonsStates]);

  // useEffect(() => {

  // }, [isControllerConnected])

  const handleStickMove = (axisState: AxisStates) => {
    switch (axisState.axisName) {
      case "LeftStickY":
        if (
          axisState.value - axisStates.LeftStickY >= 0.2 ||
          axisStates.LeftStickY - axisState.value >= 0.2
        ) {
          if (axisState.value >= 0) console.log("up");
          else console.log("down");
        } else return false;
        break;
      case "LeftStickX":
        if (
          axisState.value - axisStates.LeftStickX < 0.2 ||
          axisStates.LeftStickX - axisState.value < 0.2
        ) {
          if (axisState.value >= 0) console.log("rotateRight");
          else console.log("rotateLeft");
        } else return false;
        break;
      case "RightStickY":
        if (
          axisState.value - axisStates.RightStickY < 0.2 ||
          axisStates.RightStickY - axisState.value < 0.2
        ) {
          if (axisState.value >= 0) console.log("forward");
          else console.log("backward");
        } else return false;
        break;
      case "RightStickX":
        if (
          axisState.value - axisStates.RightStickX < 0.2 ||
          axisStates.RightStickX - axisState.value < 0.2
        ) {
          if (axisState.value >= 0) console.log("right");
          else console.log("left");
        } else return false;
        break;
      default:
        break;
    }
    return true;
  };

  const handleClick = (action: string) => {
    switch (action) {
      case "up":
        console.log("up");
        break;
      case "down":
        console.log("down");
        break;
      case "right":
        console.log("right");
        break;
      case "left":
        console.log("left");
        break;
      case "rotateRight":
        console.log("rotateRight");
        break;
      case "rotateLeft":
        console.log("rotateLeft");
        break;
      case "forward":
        console.log("forward");
        break;
      case "backward":
        console.log("backward");
        break;

      default:
        break;
    }
  };

  const handleTakePicture = () => {
    console.log("test");
  };

  return (
    <div className={style.controls}>
      <div className={style.moveControls + " " + style.left}>
        <div style={{ gridArea: "up" }}>
          <ControlButton icon={up} action={handleClick} actionType="up" />
        </div>
        <div style={{ gridArea: "left" }}>
          <ControlButton
            icon={rotateLeft}
            action={handleClick}
            actionType="rotateLeft"
          />
        </div>
        <div style={{ gridArea: "down" }}>
          <ControlButton icon={down} action={handleClick} actionType="down" />
        </div>
        <div style={{ gridArea: "right" }}>
          <ControlButton
            icon={rotateRight}
            action={handleClick}
            actionType="rotateRight"
          />
        </div>
      </div>
      <div className={style.utilsButtons}>
        <button className={style.captureBtn} onClick={handleTakePicture}>
          <img src={camera} alt="camera" draggable={false} />
        </button>
        <div className={style.controllerStatus}>
          <img
            src={isControllerConnected ? controllerActive : controllerInactive}
            alt="controller"
            draggable={false}
          />
          <GamePad
            onButtonChange={handleButtonChange}
            onConnectChange={handleConnectController}
            onAxisChange={handleAxisChange}
          />
        </div>
      </div>

      <div className={style.moveControls + " " + style.right}>
        <div style={{ gridArea: "up" }}>
          <ControlButton
            icon={forward}
            action={handleClick}
            actionType="forward"
          />
        </div>
        <div style={{ gridArea: "left" }}>
          <ControlButton
            icon={tiltLeft}
            action={handleClick}
            actionType="left"
          />
        </div>
        <div style={{ gridArea: "down" }}>
          <ControlButton
            icon={backward}
            action={handleClick}
            actionType="backward"
          />
        </div>
        <div style={{ gridArea: "right" }}>
          <ControlButton
            icon={tiltRight}
            action={handleClick}
            actionType="right"
          />
        </div>
      </div>
    </div>
  );
};

export default Controls;
