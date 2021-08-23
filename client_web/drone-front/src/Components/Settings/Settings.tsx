import React, { useState } from "react";
import style from "./Settings.module.scss";
import { Modal, Button } from "..";
import settingsGear from "../../Assets/Images/settings.svg";

type Props = {
    onSubmit: (velocity: number) => void;
};

const Settings = ({ onSubmit }: Props) => {
    const [velocity, setVelocity] = useState(5);
    const [isActive, setisActive] = useState<Boolean>(false);

    const handleClick = () => {
        setisActive(!isActive);
    };

    const handleClose = () => {
        setisActive(false);
    };

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        let vel = parseInt(e.target.value);
        if (vel > 100) vel = 100;
        if (vel < 0) vel = 0;
        setVelocity(vel);
    };

    const handleSubmit = () => {
        alert(velocity + " !");
        onSubmit(velocity);
    };

    return (
        <>
            <button className={style.settingsBtn} onClick={handleClick}>
                <img
                    src={settingsGear}
                    alt="settings"
                    className={style.settingsImg}
                    draggable={false}
                />
            </button>
            {isActive && (
                <Modal title="Paramètres" onClose={handleClose}>
                    <div className={style.inputGroup}>
                        <label className={style.inputLabel}>
                            Vitesse (en cm/s)
                        </label>
                        <input
                            className={style.input}
                            type="number"
                            max="100"
                            min="0"
                            onChange={(e) => handleChange(e)}
                        />
                        <Button
                            text="Valider"
                            action={handleSubmit}
                            className={style.submit}
                        />
                    </div>
                </Modal>
            )}
        </>
    );
};

export default Settings;
