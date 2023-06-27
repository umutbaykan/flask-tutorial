import "./Board.css";
import React, { useContext, useEffect, useMemo } from "react";
import Cell from "../Cell/Cell";

import { GameStateContext } from "../../../../App";

const Board = () => {
  const [gameState, ] = useContext(GameStateContext);

  const parsedBoard = useMemo(() => {
    if (!gameState) {return {}}
    const ships = gameState.boards[0].ships;
    let result = {};
    ships.forEach((ship) => {
      const { coordinates, alive } = ship;
      coordinates.forEach((coordinate, index) => {
        const status = alive[index] ? {class: ship.name, symbol: ""} : {class: ship.class, symbol: "X"};
        result[JSON.stringify(coordinate)] = status;
      });
    });
    return result;
  }, [gameState])

  useEffect(() => {
    console.log(gameState);
    console.log(parsedBoard)
  }, [gameState]);

  if (!gameState) {
    return null;
  }

  return (
    <>
      <h1>Board</h1>
      <div className="grid-container">
        {Array.from({ length: gameState.boards[0].size }, (_, rowIndex) => (
          <div className="row" key={rowIndex}>
            {Array.from({ length: gameState.boards[0].size }, (_, colIndex) => (
              <Cell
                key={colIndex}
                coordinates={[rowIndex, colIndex]}
                display={(parsedBoard[JSON.stringify([rowIndex, colIndex])] || {}).symbol }
                type={(parsedBoard[JSON.stringify([rowIndex, colIndex])] || {}).class }
              />
            ))}
          </div>
        ))}
      </div>
    </>
  );
};

export default Board;
