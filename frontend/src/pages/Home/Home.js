import React, { useState } from 'react';
import propTypes from "prop-types";
import NavButton from '../../components/NavButton/NavButton';

import { createRoom } from "../../services/room";


const Home = ({ navigate }) => {

  const [error, setError] = useState("");

  //TODO - forms to pick game configurations and save it as a state to send to server
  const gameconfigs = {"arraySize":10, "ships":['1','2','3']}

  const handleSubmit = async () => {
    const result = await createRoom(gameconfigs);
    if (result.success) {
      navigate(`/game/${result.room}`);
    } else {
      setError(result.error);
      navigate("/");
    }
  }

  return (
  <>
  <h1>welcome home</h1>
  <div>
  <NavButton to={'/signup'} text={'Sign Up'}/>
  <br></br>
  <NavButton to={'/login'} text={'Login'}/>
  </div>
  <button onClick={handleSubmit}>Create Game</button>
  <p>{error}</p>
  </>
  )
}

Home.propTypes = { navigate: propTypes.func };

export default Home