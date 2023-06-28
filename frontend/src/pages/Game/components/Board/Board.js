import "./Board.css";
import propTypes from "prop-types";
import React, { useContext, useEffect, useMemo } from "react";
import Cell from "../Cell/Cell";

import { GameStateContext } from "../../../../App";

const Board = ({ boardIndex, action }) => {
  const [gameState] = useContext(GameStateContext);

  const parsedBoard = useMemo(() => {
    if (!gameState) {
      return {};
    }
    const ships = gameState.boards[boardIndex].ships;
    let result = {};
    ships.forEach((ship) => {
      const { coordinates, alive } = ship;
      coordinates.forEach((coordinate, index) => {
        const status = alive[index]
          ? { class: ship.name, symbol: "" }
          : { class: ship.class, symbol: "X" };
        result[JSON.stringify(coordinate)] = status;
      });
    });
    return result;
  }, [gameState]);

  useEffect(() => {
    console.log(gameState);
    console.log(parsedBoard);
  }, [gameState]);

  return (
    <>
      <h1>Board</h1>
      <div className="grid-container">
        {Array.from(
          { length: gameState.boards[boardIndex].size },
          (_, rowIndex) => (
            <div className="row" key={rowIndex}>
              {Array.from(
                { length: gameState.boards[boardIndex].size },
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

Board.propTypes = { boardIndex: propTypes.number, action: propTypes.func };

export default Board;
