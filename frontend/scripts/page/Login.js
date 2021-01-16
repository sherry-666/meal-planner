import React, { useState, useEffect } from "react";
import { useHistory } from "react-router-dom";


export default function Login() {
    const [username, setUsername] = useState()
    const [password, setPassword] = useState()
    let history = useHistory();

    function onUsernameChange(e) {
        setUsername(e.target.value)
    }

    function onPasswordChange(e) {
        setPassword(e.target.value)
    }

    function logIn(e) {
        e.preventDefault();
		fetch(
		  "api/auth/login",
		  {
		    method: "POST",
		    body: JSON.stringify({
		      username,
		      password
		    })
		  }
		).then(res => res.json())
		 .then(
			(result) => {
			  if (result.success) {
			    history.push("/home");
			    history.go(0);
			  }else{
			    M.toast({html: 'Password or Username is not correct'})
			  }
			},
			(error) => {
			  //TODO: send alert on log in failed
			  console.log(error)
			}
		  )
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
                      <input
                        id="username" type="text" class="validate"
                        value={username} onChange={onUsernameChange}
                      />
                      <label for="username">Username</label>
                    </div>
                  </div>
                  <div class="row">
                    <div class="input-field col s12">
                      <input
                        id="password" type="password" class="validate"
                        value={password} onChange={onPasswordChange}
                      />
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


