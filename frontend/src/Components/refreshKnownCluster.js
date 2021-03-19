import React, { useRef, useState } from 'react';
import { Button } from 'react-bootstrap';
import { TextField } from '@material-ui/core';
import axios from 'axios';
import ClusterNInfo from './ClusterNInfo.js'



function RefreshField(){
	const valueRef = useRef('') 
   const [, updateState] = React.useState();
  const forceUpdate = React.useCallback(() => updateState({}), []); 
    var someVarName = JSON.stringify(valueRef.current.value)
localStorage.setItem("someVarKey", someVarName);
    function sendValue(){
        return valueRef.current.value 
    }
    function RefreshPage() {
      const cur = valueRef.current.value
      return  <ClusterNInfo clusterN = {cur}/>
   } 
    return(
	<div>
           <TextField required id="standard-required" label="Required" defaultValue= {localStorage.getItem("someVarKey")} inputRef= {valueRef}/>
           <Button onClick={forceUpdate}>Refresh</Button>
	   <RefreshPage /> 
   	</div>
    ); 
}



export default RefreshField; 
