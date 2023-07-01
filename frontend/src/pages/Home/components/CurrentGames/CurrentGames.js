import React, { useContext } from "react";

import JoinGameButton from "../../../../components/JoinGameButton/JoinGameButton";
import AllowedShipDisplayer from "../../../../components/AllowedShipDisplayer/AllowedShipDisplayer";

import { LobbyContext } from "../../../../App";

export const CurrentGames = () => {
  const currentGames = useContext(LobbyContext);

  return (
    <>
      <h3>Current available games:</h3>
      {Object.keys(currentGames).map((key) => (
        <div key={key}>
          <JoinGameButton game_id={key} load={false} />
          <p>Host: {currentGames[key].players}</p>
          <p>Player {currentGames[key].who_started + 1} starts</p>
          <AllowedShipDisplayer allowedShips={currentGames[key].allowed_ships}/>
        </div>
      ))}
    </>
  );
};

export default CurrentGames;
