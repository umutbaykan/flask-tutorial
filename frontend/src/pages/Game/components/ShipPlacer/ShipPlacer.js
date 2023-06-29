import React, { useContext } from "react";
import propTypes from "prop-types";
import { GameStateContext } from "../../../../App";

import Board from "../Board/Board";
import VirtualBoard from "../../../../utils/VirtualBoard";

import { socket } from "../../../../socket";

const ShipPlacer = ({ boardInfo }) => {
  const [gameState] = useContext(GameStateContext);

  const placeShipsRandomly = () => {
    let boardSize = gameState.boards[boardInfo.index].size;
    let allowedShips = gameState.allowed_ships;
    let vb = new VirtualBoard(boardSize, allowedShips)
    vb.randomize()
    socket.emit("place_ships", {
      ships: vb.ships,
      room: gameState.game_id,
    });
  };

  // This is going to subtract the ships in the game state from the allowed ones to get results
  const availableShips = gameState.allowed_ships;

  return (
    <div>
      <Board boardInfo={boardInfo} action={() => {}} />
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
    </div>
  );
};

ShipPlacer.propTypes = { boardInfo: propTypes.object, index: propTypes.number };

export default ShipPlacer;
