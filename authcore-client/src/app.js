'use strict';
/*
 * Demo client side SPA.
 */

import * as BS from 'react-bootstrap';
import React from 'react';
import {render} from 'react-dom';

import {Router, Route, Link} from 'react-router';


class App extends React.Component {
    render() {
        return (
            <div>
                <BS.Navbar inverse staticTop>
                    <BS.Navbar.Header>
                        <BS.Navbar.Brand>
                            <a href="#">Authcore Client</a>
                        </BS.Navbar.Brand>
                        <BS.Navbar.Toggle/>
                    </BS.Navbar.Header>

                    <BS.Navbar.Collapse>
                        <BS.Nav>
                            <BS.NavItem eventKey={1}>Link</BS.NavItem>
                            <BS.NavDropdown eventKey={2} title="Dropdown" id="basic-nav-dropdown">
                                <BS.MenuItem eventKey={2.1}>Action</BS.MenuItem>
                                <BS.MenuItem eventKey={2.2}>Another action</BS.MenuItem>
                                <BS.MenuItem eventKey={2.3}>Something else here</BS.MenuItem>
                                <BS.MenuItem divider />
                                <BS.MenuItem eventKey={2.3}>Separated link</BS.MenuItem>
                            </BS.NavDropdown>
                        </BS.Nav>

                        <BS.Navbar.Text pullRight>
                            <Link to="/login">Login</Link>
                        </BS.Navbar.Text>
                    </BS.Navbar.Collapse>
                </BS.Navbar>

                <BS.Grid fluid>
                    <BS.Row>
                        <BS.Col xs={0} sm={0} md={2} lg={2}/>
                        <BS.Col xs={12} sm={12} md={8} lg={8}>
                            <BS.PageHeader>Authcore Client</BS.PageHeader>
                            {/* The router will figure out the children for us. */}
                            {this.props.children}
                        </BS.Col>
                        <BS.Col xs={0} sm={0} md={2} lg={2}/>
                    </BS.Row>
                </BS.Grid>
            </div>
        );
    }
}


class Login extends React.Component {
    render() {
        return (
            <h3>Login</h3>
        )
    }
}


render((
    <Router>
        <Route path="/" component={App}>
            <Route path="login" component={Login}/>
        </Route>
    </Router>
), document.getElementById('app'));
