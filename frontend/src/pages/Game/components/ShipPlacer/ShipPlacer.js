import React, { useContext } from "react";
import { GameStateContext } from "../../../../App";

// Remove import from below //
const shipPositions = require("../../../model_objects/ship_placement_multiple.json");
const shipPositions2 = require("../../../model_objects/ship_placement_alternative.json");

// REvemo import from above

import { socket } from "../../../../socket";

const ShipPlacer = () => {
  const [gameState] = useContext(GameStateContext);
  const shipConfigs = shipPositions;
  const shipConfigs2 = shipPositions2;

  const handleShipPlacement = (event) => {
    event.preventDefault();
    socket.emit("place_ships", { ships: shipConfigs, room: gameState.game_id });
  };

  const handleShipPlacement2 = (event) => {
    event.preventDefault();
    socket.emit("place_ships", {
      ships: shipConfigs2,
      room: gameState.game_id,
    });
  };

  return (
    <>
      <button onClick={handleShipPlacement}>Place Alt1</button>
      <button onClick={handleShipPlacement2}>Place Alt2</button>
    </>
  );
};

export default ShipPlacer;
