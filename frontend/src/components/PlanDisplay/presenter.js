import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.scss";


const PlanDisplay = (props, context) => (
  <div className={styles.container}>
    <div className={styles.column}>
      <div className={styles.eventStatus}>{props.plan.eventstatus}</div>
    </div>
    <div className={styles.column}>
      <div className={styles.row}>
        <div className={styles.eventName}>{props.plan.eventname}</div>
        <div className={styles.eventDate}>{props.plan.eventstartlocaldate}</div>
        {props.plan.venue ? (
          <div>
            <span className={styles.venue}>{props.plan.venue.venuename}, </span>
            <span className={styles.venue}>{props.plan.venue.venuecity}</span>
          </div>
        ) : (
          <div className={styles.venue}>{context.t("Not specified")}</div>
        )}
      </div>
    </div>
    <div className={styles.column}>
      <button className={styles.button} onClick={props.handleClick}>
        {props.plan.is_planned ? context.t("Delete") : context.t("Add")}
      </button>
    </div>
  </div>
)

PlanDisplay.contextTypes = {
  t: PropTypes.func.isRequired
}

PlanDisplay.propTypes = {
  plan: PropTypes.shape({
    eventid: PropTypes.string.isRequired,
    eventname: PropTypes.string.isRequired,
    eventstartlocaldate: PropTypes.string,
    eventimageurl: PropTypes.string.isRequired,
    primaryeventurl: PropTypes.string.isRequired,
    eventstatus: PropTypes.string,
    maxprice: PropTypes.number,
    minprice: PropTypes.number,
    artists: PropTypes.arrayOf(
      PropTypes.shape({
        artistid: PropTypes.string.isRequired,
        artistname: PropTypes.string.isRequired,
        imageurl: PropTypes.string
      })
    ),
    venue: PropTypes.shape({
      venueid: PropTypes.string,
      venuename: PropTypes.string,
      venuecity: PropTypes.string,
      venuestreet: PropTypes.string
    }),
    is_planned: PropTypes.bool.isRequired
  }),
  handleClick: PropTypes.func.isRequired
}

export default PlanDisplay;
