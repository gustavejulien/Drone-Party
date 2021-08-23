export type ButtonsStates = {
  buttonName: string;
  isPressed: boolean;
};

export type AxisStates = {
  axisName: string;
  value: number;
};

export type ControllerButtons = {
  A: boolean;
  B: boolean;
  X: boolean;
  Y: boolean;
  Start: boolean;
  Back: boolean;
  LT: boolean;
  RT: boolean;
  LB: boolean;
  RB: boolean;
  LS: boolean;
  RS: boolean;
  Up: boolean;
  Down: boolean;
  Left: boolean;
  Right: boolean;
};

export type ControllerAxisValues = {
  LeftStickX: number;
  LeftStickY: number;
  RightStickX: number;
  RightStickY: number;
};
