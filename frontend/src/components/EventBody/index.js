import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.scss";

const EventBody = props => (
  <div className={styles.eventbody}>
    <p className={styles.text}>{props.eventname}</p>
    <ul>
      {props.artists.map(artist => (
        <Artist artistname={artist.artistname} key={artist.artistid} />
      ))}
    </ul>
    {props.venue && (
      <div>
        <span className={styles.text}>{props.venue.venuename}</span>
        <span className={styles.text}>, {props.venue.venuecity}</span>
      </div>
    )}
    <p className={styles.text}>{props.eventstartlocaldate}</p>
    <p className={styles.text}>{props.eventstatus}</p>
  </div>
);

const Artist = props => (
  <li>
    <span>{props.artistname}</span>
  </li>
)

EventBody.proptypes = {
  eventname: PropTypes.string.isRequired,
  eventstartlocaldate: PropTypes.string,
  eventstatus: PropTypes.string,
  artists: PropTypes.arrayOf(
    PropTypes.shape({
      artistid: PropTypes.string.isRequired,
      artistname: PropTypes.string.isRequired,
      imageurl: PropTypes.string
    })
  ),
  venue: PropTypes.shape({
    venueid: PropTypes.string.isRequired,
    venuename: PropTypes.string.isRequired,
    venuecity: PropTypes.string.isRequired,
    venuestreet: PropTypes.string
  })
}

export default EventBody;
