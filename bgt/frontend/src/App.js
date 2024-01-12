import React, { Component } from 'react';
import axios from 'axios';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = { 
      bebes: [] 
    };
  }

  componentDidMount(){
    this.getBebes()
  }

  getBebes(){
    axios
      .get('http://127.0.0.1:8000/api/bebes')
      .then(respuesta => {
        this.setState({bebes: respuesta.data});
      })
      .catch(error => {
        console.log(error);
      });
  }
  
  render() {
    return (
      <div>
        {this.state.bebes.map(item => (
        <div key={item.usuario}>
        <h1>{item.nombre} {item.apellidos}</h1>
        <ul>
          <li>Fecha de nacimiento: {item.fecha_nacimiento}</li>
          <li>Sexo: {item.sexo}</li>
          <li>Fecha: {item.fecha}</li>
        </ul>
        </div>
        ))}
      </div>
    );
  }
}
export default App;