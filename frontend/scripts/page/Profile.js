import React, { useState, useEffect, useRef } from "react";
import FamilyMember from "../component/FamilyMember.js";
import AddFamilyMember from "../component/AddFamilyMember.js";
import M from "materialize-css";

export default function Profile() {
    const [profile, setProfile] = useState()
    const [familyMembers, setFamilyMembers] = useState([])
    const profileModal = useRef()
    useEffect(() => {
        M.Modal.init(profileModal.current)
    })

    useEffect(() => {
		fetch("api/profile")
		  .then(res => res.json())
		  .then(
			(result) => {
			  console.log(result)
			  setProfile(result)
			},
			(error) => {
			  console.log(error)
			}
		  )
		setProfile({
            "family_name": "JJ",
             "total_cal" : 1000
        })
        setFamilyMembers([
                {
                "name": "Jing",
                "weight": 106,
                "height": 186,
                "year_of_birth":1994,
                "food allergy":[""]
                }, {
                "name": "Sherry",
                "weight": 63,
                "height": 168,
                "year_of_birth":1994,
                "food_allergy":["peanut"]
                }])
    }, [])


    console.log(profile)
    if (profile) {
        return <div class = "row">
            <div class="col s10 offset-s1" >
                <h1> {profile.family_name}</h1>
                <p> Family Total Daily Consumption {profile.total_cal}</p>
                <div class="row">
                    <div class="col s6 offset-s1" >
                        <ul class="collection" >
                            {familyMembers.map((member) => <FamilyMember member= {member}/>)}
                        </ul>
                        <button data-target="modal1" class="btn modal-trigger">
                            <i class="material-icons">add</i>
                        </button>
                        <div id="modal1" class="modal" ref={profileModal}>
                            <div class="modal-content">
                              <AddFamilyMember />
                            </div>
                            <div class="modal-footer">
                              <button class="btn waves-effect waves-light" type="submit" name="action">
                                Add Member
                                <i class="material-icons right">save</i>
                              </button>
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        </div>


    } else {
        return <>
    	  <h3>Loading</h3>
    	</>

    }

}