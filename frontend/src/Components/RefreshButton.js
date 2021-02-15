import React from 'react';
import { Button } from 'react-bootstrap';

function refreshButton(){
  
 function refreshPage() {
    window.location.reload(false);
  }
  
  return (
    <div>
      <hr />
      <Button onClick={refreshPage}>Refresh</Button>
    </div>
  );
}
export default refreshButton;