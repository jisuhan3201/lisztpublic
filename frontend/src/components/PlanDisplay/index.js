import { connect } from "react-redux";
import Container from "./container";
import { actionCreators as eventActions } from "redux/modules/events";

const mapDispatchToProps = (dispatch, ownProps) => {
  const { plan } = ownProps;
  return {
    handleClick: () => {
      if (plan.is_planned) {
        dispatch(eventActions.unplanList(plan.eventid));
      } else {
        dispatch(eventActions.planList(plan.eventid));
      }
    }
  };
};

export default connect(null, mapDispatchToProps)(Container);
