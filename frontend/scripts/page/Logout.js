import React, { useState, useEffect } from "react";
import { useHistory } from "react-router-dom";


export default function Logout(props) {
    let history = useHistory();
    fetch(
      "api/auth/logout",
      {
        method: "GET",
      }
    ).then(
        res => res.json())
     .then(
        (result) => {
          if (result.logout) {
            history.push("/login");
          }
        },
        (error) => {
          //TODO: send alert on logout failed
          console.log(error)
        }
      )
    return null

}


