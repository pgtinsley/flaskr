import React from 'react';
import { Button } from 'react-bootstrap';

function refreshButton(){
  
    function refreshPage() {
        window.location.reload(false);
    }
  
    return (
    <div>
        <Button onClick={refreshPage}>Refresh</Button>
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

