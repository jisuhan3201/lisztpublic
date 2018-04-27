// imports
import { actionCreators as userActions } from "redux/modules/user";
// actions

const SET_FEED = "SET_FEED";
const PLAN_EVENT = "PLAN_EVENT";
const UNPLAN_EVENT = "UNPLAN_EVENT";

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
// exports
const actionCreators = {
  getFeed,
  planEvent,
  unplanEvent
};

export { actionCreators };

// default reducer exports
export default reducer;
