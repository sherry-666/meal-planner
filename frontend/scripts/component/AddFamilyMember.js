import React, { useState, useEffect } from "react";


export default function AddFamilyMember() {

    return <div class="row">
            <form class="col s12">
              <div class="row">
                <div class="input-field col s6">
                  <input id="first_name" type="text" class="validate"/>
                  <label for="first_name">First Name</label>
                </div>
                <div class="input-field col s6">
                  <input id="last_name" type="text" class="validate"/>
                  <label for="last_name">Last Name</label>
                </div>
              </div>
              <div class="row">
                <div class="input-field col s4">
                  <input id="year_of_birth" type="text" class="validate"/>
                  <label for="year_of_birth">Year of Birth (YYYY)</label>
                </div>
                <div class="input-field col s4">
                  <input id="weight" type="text" class="validate"/>
                  <label for="weight">Weight</label>
                </div>
                <div class="input-field col s4">
                  <input id="height" type="text" class="validate"/>
                  <label for="height">Height</label>
                </div>
              </div>
              <div class="row">
                <div class="input-field col s12">
                  <input type="text" id="food_allergy" class="validate"/>
                  <label for="food_allergy">Food Allergy</label>
                </div>
              </div>
            </form>
          </div>

}