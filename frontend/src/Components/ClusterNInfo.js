import React, { useRef } from 'react';

import axios from 'axios';

import ListGroup from 'react-bootstrap/ListGroup'

export default class ClusterNInfo extends React.Component {
  state = {
    breakdown: [],
    num_clusters: 0,
    num_detections: 0,
    total_detections: 0
  }

  componentDidMount() {
   this.getData(); 
   setInterval(this.getData, 10000);
   } 

   getData = () => {
   if (this.props.clusterN) {
    const cluster = '/clusterN/' + this.props.clusterN
    axios.get(cluster)
      .then(res => {;
        console.log(res.data);
        this.setState({ breakdown: res.data.breakdown });
        this.setState({ num_clusters: res.data.num_clusters });
        this.setState({ num_detections: res.data.num_detections });
        this.setState({ total_detections: res.data.total_detections });
      })
   }
  else {
  const cluster = '/clusterN/2'
    axios.get(cluster)
      .then(res => {;
        console.log(res.data);
        this.setState({ breakdown: res.data.breakdown });
        this.setState({ num_clusters: res.data.num_clusters });
        this.setState({ num_detections: res.data.num_detections });
        this.setState({ total_detections: res.data.total_detections });
      })
   }

  }

  render() {
    return (
      <div> 
            <h4>Known Number of Clusters</h4>
            <p>Frames Processed: {this.state.num_detections} </p>
            <p>Total Detections: {this.state.total_detections} </p>
            <p>Clusters Found: {this.state.num_clusters} </p>
            <ListGroup>
                { this.state.breakdown.map(b => <ListGroup.Item key={b.id}> Cluster {b.id + 1}: {b.count} Detections </ListGroup.Item>)}
            </ListGroup>
        </div>
    )
  }
}
