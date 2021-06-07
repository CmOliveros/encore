// React imports
import React, {Component} from "react";
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link,
    Redirect
} from 'react-router-dom'

// Component imports
import FeedPage from "./FeedPage";
import UserPage from "./UserPage";

export default class HomePage extends Component {

    constructor(props) {
        super(props);
    }

    render() {
        return (<Router>
            <Switch>
                <Route exact path='/'><p>This is the home page</p></Route>
                <Route path='/feed' component={FeedPage} />
                <Route path='/user' component={UserPage} />
            </Switch>
        </Router>
        )}
}