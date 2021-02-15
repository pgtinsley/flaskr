import React from 'react';
import { Button } from 'react-bootstrap';

import axios from 'axios';

function refreshButton(){
  
 function refreshPage() {
    window.location.reload(false);
  }
  
  return (
    <div>
      <button onClick={refreshPage}>Refresh</button>
    </div>
  );
}
export default refreshButton; 
	/*
  handleClick() {
    axios.get('/ClusterN')
      .then(response=>response.json())
      .then(response => { 
	  console.log(response)})
  }

  render() {
      return (
	<button onClick={()=>this.handleClick()}>Refresh</button>

      )
}
}*/
