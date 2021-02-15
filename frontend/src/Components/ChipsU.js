
import React from 'react';

import axios from 'axios';

import Image from 'react-bootstrap/Image'
import ListGroup from 'react-bootstrap/ListGroup'

export default class ChipsU extends React.Component {
  state = {
    dataList: [],
  }

  componentDidMount() {
    axios.get('/getChipsU')
      .then(res => {;
//         console.log(res.data.data);
        this.setState({ dataList: res.data.data });
      })
  }
      
  render() {
    return (
        <div>
            <ListGroup>
                { this.state.dataList.map(chip => <ListGroup.Item key={chip.id}>Cluster {chip.cluster}  <Image roundedCircle alt={chip.id} src={'data:image/jpeg;base64,' + chip.chip}/></ListGroup.Item>)}
            </ListGroup>
        </div>
    )
  }
}
