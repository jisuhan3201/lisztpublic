import { connect } from "react-redux";
import { actionCreators as eventActions } from "redux/modules/events";
import Container from "./container";

const mapStateToProps = (state, ownProps) => {
  const { events: { feed } } = state;
  return {
    feed
  }
}

const mapDispatchToProps = (dispatch, ownProps) => {
  return {
    getFeed: () => {
      dispatch(eventActions.getFeed());
    }
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(Container);
