import React, { Component } from "react";
import SignupForm from "./presenter";

class Container extends Component {
  state = {
    username: "",
    password: "",
    email: "",
    fullname: ""
  }
  render(){
    const { username, password, email, fullname } = this.state;
    return (
      <SignupForm
        handleInputChange={this._handleInputChange}
        handleSubmit={this._handleSubmit}
        handleFacebookLogin={this._handleFacebookLogin}
        usernameValue={username}
        passwordValue={password}
        emailValue={email}
        fullnameValue={fullname}
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
    event.preventDefault();
    //redux action will be here
  }
  _handleFacebookLogin = response => {
    console.log(response)
  }
}

export default Container;
