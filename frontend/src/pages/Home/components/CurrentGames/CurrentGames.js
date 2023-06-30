import React, { useContext } from "react";

import JoinGameButton from "../JoinGameButton/JoinGameButton";

import { LobbyContext } from "../../../../App";

export const CurrentGames = () => {
  const currentGames = useContext(LobbyContext);

  return (
    <>
      <h3>Current available games:</h3>
      {Object.keys(currentGames).map((key) => (
        <div key={key}>
          <JoinGameButton game_id={key} load={false} />
          <p>{currentGames[key].gamestate}</p>
        </div>
      ))}
      <br></br>
    </>
  );
};

export default CurrentGames;
