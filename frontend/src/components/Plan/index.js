import { connect } from "react-redux";
import { actionCreators as eventActions } from "redux/modules/events";
import Container from "./container";

const mapStateToProps = (state, ownProps) => {
  const { events: { planList } } = state;
  return {
    planList
  };
};

const mapDispatchToProps = (dispatch, ownProps) => {
  return {
    getEventPlans: () => {
      dispatch(eventActions.getEventPlans());
    }
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(Container);
