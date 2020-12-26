import React, { useState, useEffect } from "react";


export default function Register() {
    const [username, setUsername] = useState()
    const [password, setPassword] = useState()
    const [password2, setPassword2] = useState()
    const [ifSamePassword, setIfSamePassword] = useState(true)


    function onUsernameChange(e) {
        setUsername(e.target.value)
    }

    function onPasswordChange(e) {
        setPassword(e.target.value)
        if (password2) {
            setIfSamePassword(password2 === e.target.value)
        }
    }

    function onPassword2Change(e) {
        setPassword2(e.target.value)
        setIfSamePassword(password === e.target.value)
    }


    function register(e) {
        e.preventDefault();
        if (password === password2) {
            fetch(
              "api/auth/register",
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
                  console.log(result)
                },
                (error) => {
                  console.log(error)
                }
              )
        } else {
            M.toast({html: 'Password Does not Match'})
        }
    }

    return (
      <div class="row">
        <div class="col s6 offset-s3">
          <h2 class="header">Register</h2>
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
                  <div class="row">
                    <div class="input-field col s12">
                      <input
                        id="password2" type="password" class={password2 ? (ifSamePassword ? "valid" : "invalid") : ""}
                        value={password2} onChange={onPassword2Change}
                      />
                      <label for="password2">Re-enter Password</label>
                      <span class="helper-text" data-error="Password Does not Match" data-success="Password Match"></span>
                    </div>
                  </div>
                </form>
              </div>
              <div class="card-action">
                <a href="#" onClick={register}>Register</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    )

}


