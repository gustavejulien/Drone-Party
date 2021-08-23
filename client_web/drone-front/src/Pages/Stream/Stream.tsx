import React, { useEffect, useState } from "react";
import { ModeButton, Controls, Settings } from "../../Components";
import style from "./Stream.module.scss";
import { dog, police } from "../../Assets/Images";

const Stream = () => {
  const [velocity, _setVelocity] = useState(5);
  const [activeMode, setActiveMode] = useState<"none" | "toutou" | "patrol">(
    "none"
  );

  const velocityRef = React.useRef(velocity);
  const setVelocity = (vel: number) => {
    velocityRef.current = vel;
    _setVelocity(vel);
  };

  const handleVelocity = (vel: number) => {
    setVelocity(vel);
  };

  const handleDoCommand = (command: string) => {
    console.log("http://localhost:8001/" + command + " " + velocityRef.current);
  };

  const _handleKeyDown = (event: KeyboardEvent) => {
    console.log(event.key);
    switch (event.key) {
      case "ArrowUp":
        handleDoCommand("cm/forward");
        break;
      case "ArrowDown":
        handleDoCommand("cm/backward");
        break;
      case "ArrowLeft":
        handleDoCommand("cm/left");
        break;
      case "ArrowRight":
        handleDoCommand("cm/right");
        break;
      case "Z":
        handleDoCommand("cm/up");
        break;
      case "z":
        handleDoCommand("cm/up");
        break;
      case "S":
        handleDoCommand("cm/down");
        break;
      case "s":
        handleDoCommand("cm/down");
        break;
      case "Q":
        handleDoCommand("turnLeft");
        break;
      case "q":
        handleDoCommand("turnLeft");
        break;
      case "D":
        handleDoCommand("turnRight");
        break;
      case "d":
        handleDoCommand("turnRight");
        break;
      default:
        break;
    }
  };

  useEffect(() => {
    document.addEventListener("keydown", _handleKeyDown);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const handleActiveMode = (mode: "toutou" | "patrol") => {
    mode === activeMode ? setActiveMode("none") : setActiveMode(mode);
  };

  return (
    <div className={style.stream}>
      <Settings onSubmit={handleVelocity} />
      <div className={style.topContainer}>
        <ModeButton
          icon={dog}
          isActive={activeMode === "toutou"}
          type="toutou"
          action={handleActiveMode}
        />
        <div className={style.video}></div>
        <ModeButton
          icon={police}
          isActive={activeMode === "patrol"}
          type="patrol"
          action={handleActiveMode}
        />
      </div>
      <Controls />
    </div>
  );
};

export default Stream;
