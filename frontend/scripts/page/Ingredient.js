import React, { useState, useEffect } from "react";


export default function Ingredient() {
    const [ingredients, setIngredients] = useState([])
    useEffect(() => {
		fetch("http://localhost:5000/api/ingredient/get")
		  .then(res => res.json())
		  .then(
			(result) => {
			  console.log(result)
			  setIngredients(result)
			},
			(error) => {
			  console.log(error)
			}
		  )
    }, [])
    if (ingredients.length == 0) {
    	return  <h3>Loading</h3>
    } else {
    	const ingredientList = ingredients.map((ingredient) =>
    	<tr>
    	  <td>{ingredient.name}</td>
		  <td>{ingredient.carbs}</td>
		  <td>{ingredient.fat}</td>
		  <td>{ingredient.protein}</td>
		  <td>{ingredient.cal}</td>
		 </tr>
		  );
		return <table>
		  <tr>
		    <th>Name</th>
		    <th>Carbs</th>
		    <th>Fat</th>
		    <th>Protein</th>
		    <th>Cal</th>
		  </tr>
		  {ingredientList}

		</table>
    }

}