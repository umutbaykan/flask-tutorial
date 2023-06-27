import React, { useContext } from "react";
import { GameStateContext } from "../../../../App";

// Remove import from below //
const shipPositions = require("../../../model_objects/ship_placement_multiple.json");
// REvemo import from above

import { socket } from "../../../../socket";

const ShipPlacer = () => {
  const [gameState, ] = useContext(GameStateContext);
  const shipConfigs = shipPositions;

  const handleShipPlacement = (event) => {
    event.preventDefault();
    socket.emit('place_ships', {ships: shipConfigs, room: gameState.game_id} )
  };

  return (
    <>
      <button onClick={handleShipPlacement}>Click to place ships</button>
    </>
  );
};

export default ShipPlacer;
