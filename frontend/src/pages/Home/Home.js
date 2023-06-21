import React, { useState } from "react";
import propTypes from "prop-types";
import NavButton from "../../components/NavButton/NavButton";
import CurrentGames from "./components/CurrentGames/CurrentGames";

import { createRoom } from "../../services/room";

// TODO remove
import { auth, logout } from "../../services/auth";

const Home = ({ navigate }) => {
  Home.propTypes = { navigate: propTypes.func };
  const [error, setError] = useState("");
  //TODO - forms to pick game configurations and save it as a state to send to server
  const gameconfigs = { arraySize: 10, ships: ["1", "2", "3"] };

  const handleSubmit = async () => {
    const result = await createRoom(gameconfigs);
    if (result.room) {
      navigate(`/game/${result.room}`);
    } else {
      setError(result.error);
      navigate("/");
    }
  };

  //// This section will be removed later
  const fastLogin = async () => {
    await auth("Roger", "password", "login");
  };

  const handleLogout = async () => {
    await logout();
  };
  ///// This section will be removed later

  return (
    <>
      <h1>welcome home</h1>
      <CurrentGames />
      <div>
        <NavButton to={"/signup"} text={"Sign Up"} />
        <br></br>
        <NavButton to={"/login"} text={"Login"} />
        <br></br>
        <NavButton to={"/profile"} text={"Profile"} />
        <br></br>
        <button onClick={handleLogout}>Logout</button>
      </div>
      <button onClick={handleSubmit}>Create Game</button>
      {/* Remove the button below */}
      <button onClick={fastLogin}>Fast Login</button>
      {/* Remove the button above */}
      <p>{error}</p>
    </>
  );
};


export default Home;
