import React, { Component } from 'react';
import axios from 'axios';
import './App.css';

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.withCredentials = true;
axios.defaults.headers.post['Content-Type'] = 'application/json';
const server = 'http://127.0.0.1:8000'

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      RoomID: "",
      CurFee: 0,
    }

    this.change = this.change.bind(this);
    this.post = this.post.bind(this);
    this.get = this.get.bind(this);
  }

  change(key, e) {
    this.setState({
      [key]: e.target.value
    });
  }

  async post() {
    let data = { ...this.state };
    console.log(data);
    let res = await axios.post(server + '/post/', data);
    console.log("POST RESPONSE");
    console.log(res);
  }

  async get() {
    let query = this.state.query;
    console.log(query);
    let res = await axios.get(server + '/get/');
    console.log("GET RESPONSE")
    console.log(res);
  }

  render() {
    return (
      <div className='App'>
        <input onChange={(e) => (this.change('RoomID', e))} />
        <br />
        <input onChange={(e) => (this.change('CurFee', e))} />
        <br />
        <button onClick={this.post}>post</button>
        <button onClick={this.get}>get</button>
      </div>
    )
  }

}

export default App;
