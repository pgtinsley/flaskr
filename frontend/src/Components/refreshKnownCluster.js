import React from 'react';
import { Button } from 'react-bootstrap';
import { TextField } from '@material-ui/core';

function RefreshField(){
   return(
       <TextField required id="standard-required" label="Required" defaultValue="4" />
   ); 
} 

export default RefreshField; 
