import React from "react";
import styles from "./Modal.module.scss";

type Props = {
    title: string;
    onClose: () => void;
};

const Modal: React.FC<Props> = ({ title, onClose, children }) => {
    const handleClose = () => {
        onClose();
    };

    return (
        <div className={styles.modalLayout} onClick={handleClose}>
            <div
                className={styles.modalContent}
                onClick={(e) => e.stopPropagation()}
            >
                <header className={styles.header}>
                    <p className={styles.title}>{title}</p>
                    <span className={styles.close} onClick={handleClose}>
                        &times;
                    </span>
                </header>
                {children}
            </div>
        </div>
    );
};

export default Modal;
