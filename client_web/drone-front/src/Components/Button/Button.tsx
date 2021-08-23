import React from "react";
import style from "./Button.module.scss";

type Props = {
    text: string;
    action?: () => void;
    className?: string;
};

const Button: React.FC<Props> = ({ text, action, className }) => {
    const handleClick = () => {
        action && action();
    };

    return (
        <div className={style.button + " " + className} onClick={handleClick}>
            {text}
        </div>
    );
};

export default Button;
