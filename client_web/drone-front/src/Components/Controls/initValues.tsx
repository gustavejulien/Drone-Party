import { ControllerAxisValues, ControllerButtons } from "../../Models/types";

export const defaultButtonsStates: ControllerButtons = {
  A: false,
  B: false,
  X: false,
  Y: false,
  Start: false,
  Back: false,
  LT: false,
  RT: false,
  LB: false,
  RB: false,
  LS: false,
  RS: false,
  Up: false,
  Down: false,
  Left: false,
  Right: false,
};

export const defaultAxisStates: ControllerAxisValues = {
  LeftStickX: 0,
  LeftStickY: 0,
  RightStickX: 0,
  RightStickY: 0,
};
