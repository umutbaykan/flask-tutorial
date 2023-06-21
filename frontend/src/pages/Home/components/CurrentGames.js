import React, { useContext } from "react";

import NavButton from "../../../components/NavButton/NavButton";

import { LobbyContext } from "../../../App";

export const CurrentGames = () => {
  const currentGames = useContext(LobbyContext);

  return (
    <>
      <h3>Current available games:</h3>
      {Object.keys(currentGames).map((key) => (
        <div key={key}>
          <NavButton to={`/game/${key}`} text={key} />
          <p>{currentGames[key].gamestate}</p>
        </div>
      ))}
      <br></br>
    </>
  );
};

export default CurrentGames;
