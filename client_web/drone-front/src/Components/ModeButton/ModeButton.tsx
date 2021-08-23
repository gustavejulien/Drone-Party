import React from "react";
import style from "./ModeButton.module.scss";

type Props = {
  icon: string;
  isActive: boolean;
  type: "toutou" | "patrol";
  action?: (mode: "toutou" | "patrol") => void;
};

const ModeButton: React.FC<Props> = ({ icon, isActive, type, action }) => {
  const handleClick = () => {
    action && action(type);
  };
  return (
    <div
      className={isActive ? `${style.modeBtn} ${style.active}` : style.modeBtn}
      onClick={handleClick}
    >
      <img src={icon} alt="icon" className={style.icon} draggable="false" />
    </div>
  );
};

export default ModeButton;
