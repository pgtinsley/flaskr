import React, { useRef, useState } from 'react';
import { Button } from 'react-bootstrap';
import { TextField } from '@material-ui/core';
import axios from 'axios';
import ClusterNInfo from './ClusterNInfo.js'



function RefreshField(){
   const valueRef = useRef('') 
   const [, updateState] = React.useState();
   const forceUpdate = React.useCallback(() => updateState({}), []); 
   function populateStorage(){
     const someVarName = JSON.stringify(valueRef.current.value)
     localStorage.setItem("input", someVarName);}
    function RefreshPage() {
      const cur = valueRef.current.value
      populateStorage()
      return  <ClusterNInfo clusterN = {cur}/>
   }
    return(
	<div>
           <TextField required id="standard-required" label="Required" defaultValue= {(localStorage.getItem("input")).replace(/['"]+/g, '')} inputRef= {valueRef}/>
           <Button onClick={forceUpdate}>Refresh</Button>
	   <RefreshPage /> 
   	</div>
    ); 
}



export default RefreshField; 
