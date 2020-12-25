import React, { useState, useEffect } from "react";


export default function Login() {

    function logIn(e) {
        e.preventDefault();
        console.log('The link was clicked.');
    }

    return (
      <div class="row">
        <div class="col s6 offset-s3">
          <h2 class="header">Log In</h2>
          <div class="card horizontal">
            <div class="card-stacked">
              <div class="card-content">
                <form class="col s12">
                  <div class="row">
                    <div class="input-field col s12">
                      <input id="username" type="text" class="validate"/>
                      <label for="username">Username</label>
                    </div>
                  </div>
                  <div class="row">
                    <div class="input-field col s12">
                      <input id="password" type="password" class="validate"/>
                      <label for="password">Password</label>
                    </div>
                  </div>
                </form>
              </div>
              <div class="card-action">
                <a href="#" onClick={logIn}>Log In</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    )

}


