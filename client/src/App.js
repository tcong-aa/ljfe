import React, { Component } from 'react';
import logo from './logo.svg';
import {
    HashRouter as Router,
    Route,
    Link,
    withRouter
} from 'react-router-dom';
import './App.css';

import CommunityIndexScene from './bundle/scene/CommunityIndexScene/index.js';
// import from './bundle/scene/'

import Search from './bundle/component/Search';

class Home extends Component {
  render() {
    return (
      <div className="App">
        <header>
          <div id="title">
            <h1>yo</h1>
              <div id="subtitle">小区详情</div>  
          </div>
          <Search />
        </header>
        <Route exact={ true } path='/index/:community_id' component={CommunityIndexScene} />
      </div>
    );
  }
}


class App extends Component {
    render() {
        return (
            <Router>
              <Home />
            </Router>
        );
    }
}

export default App;
