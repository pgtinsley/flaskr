import React, { useRef } from 'react';
import { Button } from 'react-bootstrap';
import { TextField } from '@material-ui/core';
import axios from 'axios';
import ClusterNInfo from './ClusterNInfo.js'

function RefreshField(){
	const valueRef = useRef('') 
   
    function sendValue(){
        return valueRef.current.value 
    }
    function RefreshPage() {
	    const cur = valueRef.current.value
	return  <ClusterNInfo clusterN = {cur}/>
   } 
    return(
	<div>
           <TextField required id="standard-required" label="Required" defaultValue="4" inputRef= {valueRef}/>
           <Button onClick={RefreshPage}>Refresh</Button>
	   <RefreshPage /> 
   	</div>
    ); 
}



export default RefreshField; 
