// imports
import { actionCreators as userActions } from "redux/modules/user";
// actions

const SET_FEED = "SET_FEED";
const PLAN_EVENT = "PLAN_EVENT";
const UNPLAN_EVENT = "UNPLAN_EVENT";
const SET_PLAN_LIST = "SET_PLAN_LIST";
const PLAN_LIST = "PLAN_LIST";
const UNPLAN_LIST = "UNPLAN_LIST";

// action creators
function setFeed(feed){
  return {
    type: SET_FEED,
    feed
  }
}

function doPlanEvent(eventId){
  return {
    type: PLAN_EVENT,
    eventId
  }
}

function doUnplanEvent(eventId){
  return {
    type: UNPLAN_EVENT,
    eventId
  }
}

function setPlanList(planList){
  return {
    type: SET_PLAN_LIST,
    planList
  }
}
function doPlanList(eventId){
  return {
    type: PLAN_LIST,
    eventId
  }
}

function doUnplanList(eventId){
  return {
    type: UNPLAN_LIST,
    eventId
  }
}

// api actions
function getFeed() {
  return (dispatch, getState) => {
    const { user: { token } } = getState();
    fetch("/user/events/", {
      headers: {
        Authorization: `JWT ${token}`
      }
    })
      .then(response => {
        if (response.status === 401) {
          dispatch(userActions.logout());
        }
        return response.json();
      })
      .then(json => {
        dispatch(setFeed(json));
      });
  };
}

function planEvent(eventId){
  return (dispatch, getState) => {
    dispatch(doPlanEvent(eventId));
    const { user: {token} } = getState()
    fetch(`/event/${eventId}/plan/`, {
      method: "POST",
      headers: {
        Authorization: `JWT ${token}`
      }
    })
    .then(response => {
      if(response.status === 401){
        dispatch(userActions.logout());
      } else if (!response.ok){
        dispatch(doUnplanEvent(eventId));
      }
    });
  };
}

function unplanEvent(eventId){
  return (dispatch, getState) => {
    dispatch(doUnplanEvent(eventId));
    const { user: {token} } = getState()
    fetch(`/event/${eventId}/unplan/`, {
      method: "DELETE",
      headers: {
        Authorization: `JWT ${token}`
      }
    })
    .then(response => {
      if(response.status === 401){
        dispatch(userActions.logout());
      } else if (!response.ok){
        dispatch(doPlanEvent(eventId));
      }
    });
  };
}

function getEventPlans(){
  return (dispatch, getState) => {
    const { user: { token } } = getState();
    fetch("/user/plans/", {
      headers: {
        Authorization: `JWT ${token}`
      }
    })
      .then(response => {
        if(response.status === 401) {
          dispatch(userActions.logout());
        }
        return response.json();
      })
      .then(json => {
        dispatch(setPlanList(json));
      });
  };
}

function planList(eventId){
  return (dispatch, getState) => {
    dispatch(doPlanList(eventId));
    const { user: {token} } = getState()
    fetch(`/event/${eventId}/plan/`, {
      method: "POST",
      headers: {
        Authorization: `JWT ${token}`
      }
    })
    .then(response => {
      if(response.status === 401){
        dispatch(userActions.logout());
      } else if (!response.ok){
        dispatch(doUnplanList(eventId));
      }
    });
  };
}

function unplanList(eventId){
  return (dispatch, getState) => {
    dispatch(doUnplanList(eventId));
    const { user: {token} } = getState()
    fetch(`/event/${eventId}/unplan/`, {
      method: "DELETE",
      headers: {
        Authorization: `JWT ${token}`
      }
    })
    .then(response => {
      if(response.status === 401){
        dispatch(userActions.logout());
      } else if (!response.ok){
        dispatch(doPlanList(eventId));
      }
    });
  };
}


// initial state
const initialState = {};

// reducer
function reducer(state = initialState, action){
  switch(action.type){
    case SET_FEED:
      return applySetFeed(state, action);
    case PLAN_EVENT:
      return applyPlanEvent(state, action);
    case UNPLAN_EVENT:
      return applyUnplanEvent(state, action);
    case SET_PLAN_LIST:
      return applySetPlanList(state, action);
    case PLAN_LIST:
      return applyPlanList(state, action);
    case UNPLAN_LIST:
      return applyUnplanList(state, action);
    default:
      return state;
  }
}
// reducer functions
function applySetFeed(state, action){
  const { feed } = action;
  return {
    ...state,
    feed
  }
};

function applyPlanEvent(state, action){
  const { eventId } = action;
  const { feed } = state;
  const updatedFeed = feed.map(event => {
    if(event.eventid === eventId) {
      return {...event, is_planned: true}
    }
    return event
  });
  return {...state, feed: updatedFeed};
}

function applyUnplanEvent(state, action){
  const { eventId } = action;
  const { feed } = state;
  const updatedFeed = feed.map(event => {
    if(event.eventid === eventId) {
      return {...event, is_planned: false}
    }
    return event
  });
  return {...state, feed: updatedFeed};
}

function applySetPlanList(state, action){
  const { planList } = action;
  return {
    ...state,
    planList
  };
}

function applyPlanList(state, action){
  const { eventId } = action;
  const { planList } = state;
  const updatedPlanList = planList.map(plan => {
    if(plan.eventid === eventId) {
      return {...plan, is_planned: true}
    }
    return plan
  });
  return {...state, planList: updatedPlanList};
}

function applyUnplanList(state, action){
  const { eventId } = action;
  const { planList } = state;
  const updatedPlanList = planList.map(plan => {
    if(plan.eventid === eventId) {
      return {...plan, is_planned: false}
    }
    return plan
  });
  return {...state, planList: updatedPlanList};
}

// exports
const actionCreators = {
  getFeed,
  planEvent,
  unplanEvent,
  getEventPlans,
  planList,
  unplanList
};

export { actionCreators };

// default reducer exports
export default reducer;
