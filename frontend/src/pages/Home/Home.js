import React, { useContext } from "react";

import CurrentGames from "./components/CurrentGames/CurrentGames";
import GameConfigForm from "./components/GameConfigForm/GameConfigForm";

import { LoggedInContext } from "../../App";

const Home = () => {
  const [loggedIn, ] = useContext(LoggedInContext);

  return (
    <>
      <CurrentGames />
      {loggedIn && <GameConfigForm />}
    </>
  );
};

export default Home;
