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
import GameEnd from "./components/GameEnd/GameEnd";

const Game = () => {
  const { pathname } = useLocation();
  const [game_id] = useState(pathname.substring(pathname.lastIndexOf("/") + 1));
  const [, setChats] = useContext(ChatContext);
  const [gameState, setGameState] = useContext(GameStateContext);
  const [error, setError] = useContext(ErrorContext);
  const [cookies, ,] = useCookies(["user_id"]);

  useEffect(() => {
    const handleUserLeaving = () => {
      socket.emit("leave", game_id);
      setGameState();
      setChats([]);
      setError("");
    };

    window.addEventListener("beforeunload", handleUserLeaving);

    return () => {
      window.removeEventListener("beforeunload", handleUserLeaving);
      handleUserLeaving();
    };
  }, []);

  const findBoardInfo = (input) => {
    const your = gameState.players.indexOf(cookies.user_id);
    const opponent = your === 0 ? 1 : 0;
    if (input === "Your") {
      return { index: your, owner: input };
    } else if (input === "Opponent") {
      return { index: opponent, owner: input };
    }
  };

  const fire = (coordinates) => {
    if (error) {
      return;
    } else
      socket.emit("fire", {
        coordinates: coordinates,
        room: gameState.game_id,
      });
  };

  const whoseTurnIsIt = (gameState) => {
    return (gameState.players.indexOf(cookies.user_id) +
      gameState.turn +
      gameState.who_started) %
      2 ===
      0
      ? "Your"
      : "Opponent";
  };

  const didIwin = () => {
    return gameState.who_won === cookies.user_id ? true : false
  }

  if (!gameState) {
    return null;
  }

  return (
    <>
      <h1>Welcome to game {game_id}</h1>
      <ChatBox />
      {gameState.ready ? (
        gameState.who_won ? (
          <GameEnd didIwin={didIwin()} />
        ) : (
          <>
            <h3>{whoseTurnIsIt(gameState)} turn.</h3>
            <Board boardInfo={findBoardInfo("Your")} action={console.log} />
            <Board boardInfo={findBoardInfo("Opponent")} action={fire} />
          </>
        )
      ) : (
        <>
          <ShipPlacer />
          <Board boardInfo={findBoardInfo("Your")} action={console.log} />
        </>
      )}
      <h3>{error}</h3>
      <br></br>
      <WhereAmI />
    </>
  );
};

export default Game;
