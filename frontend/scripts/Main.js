import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import M from 'materialize-css';
import Ingredient from "./page/Ingredient";
import Login from "./page/Login";
import Register from "./page/register";

export default function App(props) {
  return (
    <Router>
      <div>
        <nav>
            <div class="nav-wrapper">
              <a href="#" class="brand-logo">Logo</a>
              <ul id="nav-mobile" class="right hide-on-med-and-down">
                {
                  props.user ?
                  <>
                    <li>
                      <Link to="/">Home</Link>
                    </li>
                    <li>
                      <Link to="/recipe">Recipe</Link>
                    </li>
                    <li>
                      <Link to="/ingredient">Ingredient</Link>
                    </li>
                  </>
                 :
                  <>
                    <li>
                      <Link to="/login">Log In</Link>
                    </li>
                    <li>
                      <Link to="/register">Register</Link>
                    </li>
                  </>
                }
              </ul>
            </div>
        </nav>


        {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
        <Switch>
          <Route path="/recipe">
            <Recipe />
          </Route>
          <Route path="/ingredient">
            <Ingredient />
          </Route>
          <Route path="/login">
            <Login />
          </Route>
          <Route path="/register">
            <Register />
          </Route>
          <Route path="/">
            <Home user={props.user}/>
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

function Home(props) {
  return <h2>Home Page. Hello {props.user ? ` ,${props.user.username}` : ""}</h2>;
}

function Recipe() {
  return <h2>Recipe</h2>;
}
