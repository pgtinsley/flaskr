
import 'bootstrap/dist/css/bootstrap.css';

import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

import ClusterNInfo from './Components/ClusterNInfo.js' 
import ClusterUInfo from './Components/ClusterUInfo.js'

import ChipsN from './Components/ChipsN.js' 
import ChipsU from './Components/ChipsU.js' 

import RefreshButton from './Components/RefreshButton.js'
import RefreshField from './Components/refreshKnownCluster.js'
function App() {
    
    return (
        <div className="App">
            <Container className="text-center">
                <h1>Facial Recognition Dashboard</h1>
                <p>{ new Date().toLocaleTimeString() }</p>
                <Row>
                    <Col>
                <RefreshField/>     
	    	</Col>
                    <Col>
                        <ClusterUInfo />
                    </Col>
                </Row>
                <hr />
                <Row>
                    <Col>
                        <ChipsN />
                    </Col>
                    <Col>
                        <ChipsU />
                    </Col>
                </Row>
                <hr />
            </Container>
         {setTimeout('window.location.reload();', 30000)}}
	 </div>
    );
}

export default App;
