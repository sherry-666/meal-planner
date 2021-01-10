import React, { useState, useEffect } from "react";


export default function AddFamilyMember(props) {
    const [name, setName] = useState()
    const [yearOfBirth, setYearOfBirth] = useState()
    const [yearValid,setYearValid] = useState(true)
    const [weight, setWeight] = useState()
    const [height, setHeight] = useState()
    const [activityLevel, setActivityLevel] = useState()
    const [foodAllergy, setFoodAllergy] = useState()


    function saveMember(e) {
        fetch(
              "api/profile/add-member",
              {
                method: "POST",
                body: JSON.stringify({
                  username: props.user.username,
                  name,
                  yearOfBirth,
                  weight,
                  height,
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
        console.log ('save')
    }

    function onYearOfBirthBlur(e) {

        let thisYear = new Date().getFullYear()
        if (isNaN(yearOfBirth)) {
            setYearValid(false)
            console.log(yearValid)
        } else if (yearOfBirth >= thisYear || yearOfBirth <= 1900) {
            setYearValid(false)
            console.log(yearValid)
        } else {
            setYearValid(true)
        }
    }

    return <>
        <div class="modal-content">
              <div class="row">
                <form class="col s12">
                  <div class="row">
                    <div class="input-field col s6">
                      <input
                        id="name" type="text" class="validate"
                        value={name} onChange={(e) => setName(e.target.value)}
                       />
                      <label for="name">Name</label>
                    </div>
                  </div>
                  <div class="row">
                    <div class="input-field col s4">
                      <input
                        id="year_of_birth" type="text"
                        class={yearValid ? "valid" : "invalid"}
                        value={yearOfBirth}
                        onBlur={onYearOfBirthBlur}
                        onChange={(e) => setYearOfBirth(e.target.value)}
                      />
                      <label for="year_of_birth">Year of Birth (YYYY)</label>
                      <span class="helper-text" data-error="Format must be YYYY"></span>
                    </div>
                    <div class="input-field col s4">
                      <input
                        id="weight" type="text" class="validate"
                        value={weight} onChange={(e) => setWeight(e.target.value)}
                      />
                      <label for="weight">Weight (kg)</label>
                    </div>
                    <div class="input-field col s4">
                      <input
                        id="height" type="text" class="validate"
                        value={height} onChange={(e) => setHeight(e.target.value)}
                      />
                      <label for="height">Height (cm)</label>
                    </div>
                  </div>
                  <div class="row">
                    <div class="input-field col s12">
                      <input
                        type="text" id="activity_level" class="validate"
                        value={activityLevel} onChange={(e) => setActivityLevel(e.target.value)}
                      />
                      <label for="activity_level">Activity Level</label> //test branch function
                    </div>
                  </div>
                  <div class="row">
                    <div class="input-field col s12">
                      <input
                        type="text" id="food_allergy" class="validate"
                        value={foodAllergy} onChange={(e) => setFoodAllergy(e.target.value)}
                      />
                      <label for="food_allergy">Food Allergy</label>
                    </div>
                  </div>
                </form>
              </div>
            </div>
            <div class="modal-footer">
              <button
                class="btn waves-effect waves-light"
                type="submit"
                name="action"
                onClick={saveMember}
              >
                Add Member
                <i class="material-icons right" >save</i>
              </button>
        </div>
    </>
}