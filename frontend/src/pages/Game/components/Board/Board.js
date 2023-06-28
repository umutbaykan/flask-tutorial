import "./Board.css";
import propTypes from "prop-types";
import React, { useContext, useEffect, useMemo } from "react";
import Cell from "../Cell/Cell";

import { GameStateContext } from "../../../../App";

const Board = ({ boardInfo, action }) => {
  const [gameState] = useContext(GameStateContext);

  const parsedBoard = useMemo(() => {
    if (!gameState) {
      return {};
    }
    const ships = gameState.boards[boardInfo.index].ships;
    const missed_shots = gameState.boards[boardInfo.index].missed_shots;
    let result = {};
    ships.forEach((ship) => {
      const { coordinates, alive } = ship;
      coordinates.forEach((coordinate, index) => {
        const status = alive[index]
          ? { class: ship.name, symbol: "" }
          : { class: ship.name, symbol: "X" };
        result[JSON.stringify(coordinate)] = status;
      });
    });
    missed_shots.forEach((coordinate) => {
      result[JSON.stringify(coordinate)] = { class: "miss", symbol: " · " };
    });
    return result;
  }, [gameState]);

  useEffect(() => {
    console.log(gameState);
    console.log(parsedBoard);
  }, [gameState]);

  return (
    <>
      <h1>{boardInfo.owner} Board</h1>
      <div className="grid-container">
        {Array.from(
          { length: gameState.boards[boardInfo.index].size },
          (_, rowIndex) => (
            <div className="row" key={rowIndex}>
              {Array.from(
                { length: gameState.boards[boardInfo.index].size },
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
          )
        )}
      </div>
    </>
  );
};

Board.propTypes = {
  boardInfo: propTypes.object,
  action: propTypes.func,
  owner: propTypes.string,
};

export default Board;
