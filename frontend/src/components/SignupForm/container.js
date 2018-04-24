import React, { Component } from "react";
import PropTypes from "prop-types";
import SignupForm from "./presenter";

class Container extends Component {
  state = {
    username: "",
    password: "",
    email: "",
    name: ""
  }
  static propTypes = {
    facebookLogin: PropTypes.func.isRequired,
    createAccount: PropTypes.func.isRequired
  };
  render(){
    const { username, password, email, name } = this.state;
    return (
      <SignupForm
        handleInputChange={this._handleInputChange}
        handleSubmit={this._handleSubmit}
        handleFacebookLogin={this._handleFacebookLogin}
        usernameValue={username}
        passwordValue={password}
        emailValue={email}
        nameValue={name}
      />
    );
  }
  _handleInputChange = event => {
    const {target : {value, name}} = event;
    this.setState({
      [name]: value
    });
  };
  _handleSubmit = event => {
    const { username, password, email, name } = this.state;
    const { createAccount } = this.props;
    event.preventDefault();
    createAccount(username, password, email, name);
    //redux action will be here
  }
  _handleFacebookLogin = response => {
    const { facebookLogin } = this.props;
    facebookLogin(response.accessToken);
  }
}

export default Container;
