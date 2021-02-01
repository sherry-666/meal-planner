import React, { useState, useEffect, useRef } from "react";
import FamilyMember from "../component/FamilyMember.js";
import AddFamilyMember from "../component/AddFamilyMember.js";
import M from "materialize-css";
import { useHistory } from "react-router-dom";

export default function Profile(props) {
    if (!props.user) {
        let history = useHistory()
        history.push("/home")
    } else {
    //get username to pull profile.
    }
    const [profile, setProfile] = useState()
    const [familyMembers, setFamilyMembers] = useState([])
    const profileModal = useRef()
    var profileModalInstance

    const profileModalClose = () => {profileModalInstance.close()}
    useEffect(() => {
        profileModalInstance = M.Modal.init(profileModal.current)
    })

    useEffect(() => {
        console.log("api/profile/get?username=" + props.user.username)
		fetch(
		    "api/profile/get?username=" + props.user.username,
		)
		  .then(res => {
		            console.log("returning response in json")
		            return res.json()
		  })
		  .then(
			(result) => {
			  console.log("this is received profile")
			  console.log(result)
			  setProfile(result)
			  setFamilyMembers(result.family_members)
			},
			(error) => {
			  console.log(error)
			}
		  )
    }, [])


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
                        <button data-target="add-family-modal" class="btn modal-trigger">
                            <i class="material-icons">add</i>
                        </button>
                        <div id="add-family-modal" class="modal" ref={profileModal}>
                            <AddFamilyMember user={props.user} closeModal={profileModalClose}/>
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