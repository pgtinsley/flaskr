import React from 'react';

import axios from 'axios';

import ListGroup from 'react-bootstrap/ListGroup'

export default class ClusterNInfo extends React.Component {
  state = {
    breakdown: [],
    num_clusters: 0,
    num_detections: 0,
  }

  componentDidMount() {
    axios.get('/clusterN')
      .then(res => {;
        console.log(res.data);
        this.setState({ breakdown: res.data.breakdown });
        this.setState({ num_clusters: res.data.num_clusters });
        this.setState({ num_detections: res.data.num_detections });
      })
  }

  render() {
    return (
        <div>
            <h4>Known Number of Clusters</h4>
            <p>Frames Processed: {this.state.num_detections} </p>
            <p>Clusters Found: {this.state.num_clusters} </p>
            <ListGroup>
                { this.state.breakdown.map(b => <ListGroup.Item key={b.id}> Cluster {b.id + 1}: {b.count} Detections </ListGroup.Item>)}
            </ListGroup>
        </div>
    )
  }
}
