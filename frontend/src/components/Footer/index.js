import React from "react";
import styles from "./styles.scss";

const Footer = (props, context) => (
  <footer className={styles.footer}>
    <div className={styles.column}>
      <nav className={styles.nav}>
        <ul className={styles.list}>
          <li className={styles.listItem}>About Us</li>
          <li className={styles.listItem}>Privacy</li>
          <li className={styles.listItem}>Terms</li>
          <li className={styles.listItem}>Language</li>
          <li className={styles.listItem}>Contacts</li>
        </ul>
      </nav>
    </div>
    <div className={styles.column}>
      <span className={styles.copyright}>&copy; 2018 Lisztfever</span>
    </div>
  </footer>
)

export default Footer;
