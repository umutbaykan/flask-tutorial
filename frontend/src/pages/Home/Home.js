import React, { useContext } from "react";
import "./Home.css"

import CurrentGames from "./components/CurrentGames/CurrentGames";
import GameConfigForm from "./components/GameConfigForm/GameConfigForm";

import { LoggedInContext } from "../../App";

const Home = () => {
  const [loggedIn, ] = useContext(LoggedInContext);

  return (
    <div className="container">
      <CurrentGames />
      {loggedIn && <GameConfigForm />}
    </div>
  );
};

export default Home;
