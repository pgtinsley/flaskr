
import 'bootstrap/dist/css/bootstrap.css';

import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

// import PersonList from './Components/PersonList.js'
import ClusterNInfo from './Components/ClusterNInfo.js' 
import ClusterUInfo from './Components/ClusterUInfo.js' 
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
           <RefreshButton /> 
	    </Container>
	    </div>
    );
}

export default App;
