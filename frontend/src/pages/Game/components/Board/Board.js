import './Board.css'
import React, { useContext, useEffect } from "react";
import Cell from "../Cell/Cell";

import { GameStateContext } from "../../../../App";

const Board = () => {
  const [gameState, setGameState] = useContext(GameStateContext);

  useEffect(() => {
    console.log(gameState);
  }, [gameState]);

  if (!gameState) {return null}

  return (
    <>
    <h1>Board</h1>
    <div className="grid-container">
      {Array.from({ length: gameState.boards[0].size }, (_, rowIndex) => (
        <div className="row" key={rowIndex}>
          {Array.from({ length: gameState.boards[0].size }, (_, colIndex) => (
            <Cell key={colIndex} coordinates={[rowIndex, colIndex]}/>
          ))}
        </div>
      ))}
    </div>
    </>
  );
};

export default Board;
