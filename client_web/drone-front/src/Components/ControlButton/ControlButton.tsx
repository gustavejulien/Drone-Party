import React from "react";
import style from "./ControlButton.module.scss";

type Props = {
    icon: string;
    action?: (actionType: string) => void;
    actionType: string;
};

const ControlButton: React.FC<Props> = ({ icon, action, actionType }) => {
    const handleClick = () => {
        action && action(actionType);
    };

    return (
        <div className={style.controlButton} onClick={handleClick}>
            <img src={icon} alt="control" draggable="false" />
        </div>
    );
};

export default ControlButton;
