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
        <h1>Bebés</h1>
        <table border="1">
          <thead>
            <tr>
              <th>Id</th>
              <th>Imagen</th>
              <th>Nombre</th>
              <th>Fecha de nacimiento</th>
              <th>Sexo</th>
            </tr>
          </thead>
          <tbody>
            {this.state.bebes.map(item => (
              <tr key={item.usuario}>
                <td>{item.id}</td>
                <td><img src={item.imagen} alt={item.imagen} width="64" height="64"></img></td>
                <td>{item.nombre} {item.apellidos}</td>
                <td>{item.fecha_nacimiento}</td>
                <td>{item.sexo}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  }
}
export default App;