import React, { useContext } from "react";
import { GameStateContext } from "../../../../App";

// Remove import from below //
const shipPositions = require("../../../model_objects/ship_placement_multiple.json");
// REvemo import from above

import { socket } from "../../../../socket";

const ShipPlacer = () => {
  const shipConfigs = shipPositions;

  const handleShipPlacement = () => {
    console.log(shipConfigs);
    socket.emit('place_ships', {ships: shipConfigs, room: 123} )
    // socket.emit("chat", { message: message.chat, room: game_id });

  };

  return (
    <>
      <button onClick={handleShipPlacement}>Click to place ships</button>
    </>
  );
};

export default ShipPlacer;
