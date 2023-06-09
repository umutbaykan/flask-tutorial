import "./Board.css";
import propTypes from "prop-types";
import React, { useContext, useMemo } from "react";
import Cell from "../Cell/Cell";

import { GameStateContext } from "../../../../App";

const Board = ({ boardInfo, action }) => {
  const [gameState] = useContext(GameStateContext);
  const { index, owner } = boardInfo;

  const parsedBoard = useMemo(() => {
    if (!gameState) {
      return {};
    }
    const ships = gameState.boards[index].ships;
    const missed_shots = gameState.boards[index].missed_shots;
    let result = {};
    ships.forEach((ship) => {
      const { coordinates, alive } = ship;
      coordinates.forEach((coordinate, index) => {
        const status = alive[index]
          ? { class: ship.name, symbol: "" }
          : owner === "Your"
          ? { class: ship.name, symbol: "X" }
          : { class: "hit", symbol: "X" };
        result[JSON.stringify(coordinate)] = status;
      });
    });
    missed_shots.forEach((coordinate) => {
      result[JSON.stringify(coordinate)] = { class: "miss", symbol: "" };
    });
    return result;
  }, [gameState]);

  return (
    <div className="container board">
      <div className="grid-container">
        {Array.from({ length: gameState.boards[index].size }, (_, rowIndex) => (
          <div className="row" key={rowIndex}>
            {Array.from(
              { length: gameState.boards[index].size },
              (_, colIndex) => (
                <Cell
                  key={colIndex}
                  coordinates={[rowIndex, colIndex]}
                  display={
                    (parsedBoard[JSON.stringify([rowIndex, colIndex])] || {})
                      .symbol
                  }
                  type={
                    (parsedBoard[JSON.stringify([rowIndex, colIndex])] || {})
                      .class
                  }
                  action={action}
                />
              )
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

Board.propTypes = {
  boardInfo: propTypes.object,
  action: propTypes.func,
  owner: propTypes.string,
};

export default Board;
