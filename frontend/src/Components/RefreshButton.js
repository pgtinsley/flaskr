import React from 'react';
import { Button } from 'react-bootstrap';

<<<<<<< HEAD
=======
import axios from 'axios';

>>>>>>> 57eee6f4e1d6b63fac4dd4d57e6bb71c6fd04255
function refreshButton(){
  
 function refreshPage() {
    window.location.reload(false);
  }
  
  return (
    <div>
<<<<<<< HEAD
      <hr />
      <Button onClick={refreshPage}>Refresh</Button>
    </div>
  );
}
export default refreshButton;
=======
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
>>>>>>> 57eee6f4e1d6b63fac4dd4d57e6bb71c6fd04255
