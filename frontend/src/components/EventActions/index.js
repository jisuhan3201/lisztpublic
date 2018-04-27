import { connect } from "react-redux";
import Container from "./container";
import { actionCreators as eventActions } from "redux/modules/events";

const mapDispatchToProps = (dispatch, ownProps) => {
  return {
    handleCalendarClick: () => {
      if(ownProps.isPlanned) {
        dispatch(eventActions.unplanEvent(ownProps.eventId));
      } else {
        dispatch(eventActions.planEvent(ownProps.eventId));
      }
    }
  }
};

export default connect(null, mapDispatchToProps)(Container);
