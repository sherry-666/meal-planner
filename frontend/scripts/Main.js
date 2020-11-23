import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import M from 'materialize-css';
import Ingredient from "./page/Ingredient";

export default function App() {
  return (
    <Router>
      <div>
        <nav>
            <div class="nav-wrapper">
              <a href="#" class="brand-logo">Logo</a>
              <ul id="nav-mobile" class="right hide-on-med-and-down">
                <li>
                  <Link to="/">Home</Link>
                </li>
                <li>
                  <Link to="/recipe">Recipe</Link>
                </li>
                <li>
                  <Link to="/ingredient">Ingredient</Link>
                </li>
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
          <Route path="/">
            <Home />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

function Home() {
  return <h2>Home</h2>;
}

function Recipe() {
  return <h2>Recipe</h2>;
}
