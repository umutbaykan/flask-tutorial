import React, { useContext } from "react";
import propTypes from "prop-types";
import { useCookies } from "react-cookie";
import { GameStateContext } from "../../../../App";
import { ErrorContext } from "../../../../App";

import Board from "../Board/Board";
import VirtualBoard from "../../../../utils/VirtualBoard";

import { socket } from "../../../../socket";

const ShipPlacer = ({ boardInfo }) => {
  const [gameState] = useContext(GameStateContext);
  const [cookies, ,] = useCookies(["user_id"]);
  const [, setError] = useContext(ErrorContext);

  const placeShipsRandomly = () => {
    setError("");
    let boardSize = gameState.boards[boardInfo.index].size;
    let allowedShips = gameState.allowed_ships;
    let vb = new VirtualBoard(boardSize, allowedShips);
    vb.randomize();
    socket.emit("place_ships", {
      ships: vb.ships,
      room: gameState.game_id,
    });
  };

  const setReady = () => {
    if (didUserSetShips()) {
      socket.emit("ready", {
        room: gameState.game_id,
      });
    } else {
      setError("You need to place your ships.");
      return;
    }
  };

  const didUserSetShips = () => {
    const index = gameState.players.indexOf(cookies.user_id);
    if (
      gameState.boards[index].ships.length ===
      Object.keys(gameState.allowed_ships).length
    ) {
      return true;
    } else {
      return false;
    }
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
      <button onClick={setReady}>Start game!</button>
    </div>
  );
};

ShipPlacer.propTypes = { boardInfo: propTypes.object, index: propTypes.number };

export default ShipPlacer;
