import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.scss";
import EventBody from "components/EventBody";
import EventActions from "components/EventActions";


const FeedEvent = (props, context) => {
  return (
    <div className={styles.feedEvent}>
      <header>
        <img src={props.eventimageurl || require("images/noImage.jpg")} alt={props.eventname} />
      </header>
      <div>
        <EventBody
          eventname={props.eventname}
          eventstatus={props.eventstatus}
          eventstartlocaldate={props.eventstartlocaldate}
          artists={props.artists}
          venue={props.venue}
        />
      </div>
      <div>
        <EventActions isPlanned={props.is_planned} eventId={props.eventid}/>
      </div>
    </div>
  )
};

FeedEvent.propTypes = {
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
    venueid: PropTypes.string.isRequired,
    venuename: PropTypes.string.isRequired,
    venuecity: PropTypes.string.isRequired,
    venuestreet: PropTypes.string
  }),
  is_planned: PropTypes.bool.isRequired
}

export default FeedEvent;
