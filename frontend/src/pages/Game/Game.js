import React, { useState, useEffect, useContext } from "react";
import { useLocation } from "react-router-dom";
import { socket } from "../../socket";
import { useCookies } from "react-cookie";

import { GameStateContext } from "../../App";
import { ChatContext } from "../../App";
import { ErrorContext } from "../../App";

import WhereAmI from "../../components/whereami/whereami";
import ChatBox from "./components/ChatBox/ChatBox";
import ShipPlacer from "./components/ShipPlacer/ShipPlacer";
import Board from "./components/Board/Board";

const Game = () => {
  const { pathname } = useLocation();
  const [game_id] = useState(pathname.substring(pathname.lastIndexOf("/") + 1));
  const [, setChats] = useContext(ChatContext);
  const [gameState, setGameState] = useContext(GameStateContext);
  const [error] = useContext(ErrorContext);
  const [cookies, ,] = useCookies(["user_id"]);

  useEffect(() => {
    const handleUserLeaving = () => {
      socket.emit("leave", game_id);
      setGameState();
      setChats([]);
    };

    window.addEventListener("beforeunload", handleUserLeaving);

    return () => {
      window.removeEventListener("beforeunload", handleUserLeaving);
      handleUserLeaving();
    };
  }, []);

  //// Remove section below
  const handleClick = (event) => {
    event.preventDefault();
    console.log(gameState);
  };
  ////

  const findBoardIndex = (input) => {
    const own = gameState.players.indexOf(cookies.user_id);
    const opponent = own === 0 ? 1 : 0;
    if (input === "own") {
      return own;
    } else if (input === "opponent") {
      return opponent;
    }
  };

  if (!gameState) {
    return null;
  }

  return (
    <>
      <h1>Welcome to game {game_id}</h1>
      <ChatBox />
      {gameState.ready ? (
        <>
          <Board boardIndex={findBoardIndex("own")} action={() => {}} />
          <Board boardIndex={findBoardIndex("opponent")} action={() => {}} />
        </>
      ) : (
        <>
          <ShipPlacer />
          <Board boardIndex={findBoardIndex("own")} action={() => {}} />
        </>
      )}
      <br></br>
      <h3>Development section</h3>
      <button onClick={handleClick}>print game state</button>
      <h3>{error}</h3>
      <WhereAmI />
    </>
  );
};

export default Game;
