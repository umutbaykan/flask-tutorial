import React, { useContext } from "react";
import propTypes from "prop-types";
import { GameStateContext } from "../../../../App";

import Board from "../Board/Board";

import { randomize } from "../../../../utils/randomize";

// Remove import from below //
const shipPositions = require("../../../model_objects/ship_placement_single.json");
const shipPositions2 = require("../../../model_objects/ship_placement_single_alternative.json");

// REvemo import from above

import { socket } from "../../../../socket";

const ShipPlacer = ({ boardInfo }) => {
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

  const placeShipsRandomly = () => {
    // Will randomize using a helper function
    let size = gameState.boards[boardInfo.index].size;
    let allowed_ships = gameState.allowed_ships;
    const result = randomize(size, allowed_ships);
    // Function will take those above and randomize accordingly
    // Should return a JSON in the correct format

    // Will emit for now but probably emit will be moved to the start button later
  };

  // This is going to subtract the ships in the game state from the allowed ones to get results
  const availableShips = gameState.allowed_ships;

  return (
    <div>
      <Board boardInfo={boardInfo} action={console.log} />
      <div>
        <h1>Allowed Ships</h1>
        <ul>
          {Object.entries(availableShips).map(([ship, quantity]) => (
            <ul key={ship}>
              {ship} - {quantity}
            </ul>
          ))}
        </ul>
      </div>
      <button onClick={placeShipsRandomly}>Randomize!</button>
      <button onClick={handleShipPlacement}>Place Alt1</button>
      <button onClick={handleShipPlacement2}>Place Alt2</button>
    </div>
  );
};

ShipPlacer.propTypes = { boardInfo: propTypes.object, index: propTypes.number };

export default ShipPlacer;
