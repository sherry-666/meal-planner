import React from "react";
import ReactDOM from "react-dom";
import Main from "./Main";

var rootNode = document.getElementById("react-root")
ReactDOM.render(<Main user={JSON.parse(rootNode.dataset.user)}/>, rootNode);
