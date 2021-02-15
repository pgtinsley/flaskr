
import 'bootstrap/dist/css/bootstrap.css';

import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

// import PersonList from './Components/PersonList.js'
import ClusterNInfo from './Components/ClusterNInfo.js' 
<<<<<<< HEAD
import ClusterUInfo from './Components/ClusterUInfo.js'
import ChipsN from './Components/ChipsN.js' 
import ChipsU from './Components/ChipsU.js' 

=======
import ClusterUInfo from './Components/ClusterUInfo.js' 
>>>>>>> 57eee6f4e1d6b63fac4dd4d57e6bb71c6fd04255
import RefreshButton from './Components/RefreshButton.js'

function App() {
    
    return (
        <div className="App">
            <Container className="text-center">
                <h1>Facial Recognition Dashboard</h1>
                <p>{ new Date().toLocaleTimeString() }</p>
                <Row>
                    <Col>
                        <ClusterNInfo />
                    </Col>
                    <Col>
                        <ClusterUInfo />
                    </Col>
                </Row>
<<<<<<< HEAD
                <hr />
                <Row>
                    <Col>
                        <ChipsN />
                    </Col>
                    <Col>
                        <ChipsU />
                    </Col>

                </Row>
                <RefreshButton /> 
            </Container>
        </div>
=======
           <RefreshButton /> 
	    </Container>
	    </div>
>>>>>>> 57eee6f4e1d6b63fac4dd4d57e6bb71c6fd04255
    );
}

export default App;
