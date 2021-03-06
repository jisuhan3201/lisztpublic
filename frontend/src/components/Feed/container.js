import React, { Component } from "react";
import PropTypes from "prop-types";
import Feed from "./presenter";

class Container extends Component {
  state = {
    loading: true
  };
  static propTypes = {
    getFeed: PropTypes.func.isRequired,
    feed: PropTypes.array
  };
  componentDidMount() {
    const { getFeed } = this.props;
    if(!this.props.feed){
      getFeed();
    } else {
      this.setState({
        loading: false
      });
    }
  }

  componentDidUpdate = (prevProps, prevState) => {
    const { getFeed } = this.props;
    console.log(prevProps, this.props)
  }

  componentWillReceiveProps = (nextProps) => {
    if (nextProps.feed) {
      this.setState({
        loading: false
      });
    }
  }
  render(){
    const { feed } = this.props;
    return <Feed {...this.state} feed={feed} />;
  }
}

export default Container;
