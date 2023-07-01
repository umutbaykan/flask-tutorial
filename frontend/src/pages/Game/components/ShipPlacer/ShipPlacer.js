import React, { useContext, useState } from "react";
import propTypes from "prop-types";
import { useCookies } from "react-cookie";
import { GameStateContext } from "../../../../App";
import { ErrorContext } from "../../../../App";

import Board from "../Board/Board";
import VirtualBoard from "../../../../utils/VirtualBoard";

import { socket } from "../../../../socket";
import AllowedShipDisplayer from "../../../../components/AllowedShipDisplayer/AllowedShipDisplayer";

const ShipPlacer = ({ boardInfo }) => {
  const [gameState] = useContext(GameStateContext);
  const [cookies, ,] = useCookies(["user_id"]);
  const [error, setError] = useContext(ErrorContext);
  const [startClicked, setStartClicked] = useState(false);

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
      setError("");
      setStartClicked(true);
    } else {
      setError("You need to place your ships.");
      return;
    }
  };

  const didUserSetShips = () => {
    const index = gameState.players.indexOf(cookies.user_id);
    if (
      gameState.boards[index].ships.length ===
      Object.values(gameState.allowed_ships).reduce(
        (sum, value) => sum + value,
        0
      )
    ) {
      return true;
    } else {
      return false;
    }
  };

  // TODO
  // Add a way to display the number of remaining ships in user's allowed ships

  return (
    <div className="container ship-placer">
      <div className="container board-header">
        <h4>Your board</h4>
        <Board boardInfo={boardInfo} action={() => {}} />
      </div>
      <div className="container placement-area">
        <h4>Place your ships, captain.</h4>
        <p>
          Available ships are displayed below. Once you are ready, hit the start
          game button and start the game.
        </p>
        <AllowedShipDisplayer allowedShips={gameState.allowed_ships} />
        {startClicked ? (
          <h4>Waiting for opponent.</h4>
        ) : (
          <>
            <button className="button-regular" onClick={placeShipsRandomly}>
              Randomize!
            </button>
            <button className="button-join" onClick={setReady}>
              Start game!
            </button>
          </>
        )}

        <p className="error">{error}</p>
      </div>
    </div>
  );
};

ShipPlacer.propTypes = { boardInfo: propTypes.object, index: propTypes.number };

export default ShipPlacer;
