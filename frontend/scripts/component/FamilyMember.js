import React, { useState, useEffect } from "react";

export default function FamilyMember(props) {
    var member = props.member

    return <li class="collection-item avatar">
              <i class="material-icons circle large">accessibility</i>
              <span class="title"><b>{member.name}</b></span>
              <p><b>Year</b>: {member.year_of_birth}     <b>Weight</b>: {member.weight}    <b>Height</b>: {member.height} <br/>
                 <b>Food Allergy</b>: {member.food_allergy}
              </p>
              <a href="#!" class="secondary-content">
                <i class="material-icons">edit</i>
                <i class="material-icons">home</i>
              </a>
            </li>
}