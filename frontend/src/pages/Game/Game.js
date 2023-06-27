import React, { useState, useEffect, useContext } from "react";
import { useLocation } from "react-router-dom";
import { socket } from "../../socket";

import { GameStateContext } from "../../App";
import { ChatContext } from "../../App";
import { ErrorContext } from "../../App";

import WhereAmI from "../../components/whereami/whereami";
import ChatBox from "./components/ChatBox/ChatBox";
import ShipPlacer from "./components/ShipPlacer/ShipPlacer";


const Game = () => {
  const { pathname } = useLocation();
  const [game_id] = useState(pathname.substring(pathname.lastIndexOf("/") + 1));
  const [ , setChats] = useContext(ChatContext);
  const [gameState, ] = useContext(GameStateContext);
  const [error, ] = useContext(ErrorContext)

  useEffect(() => {
    const handleUserLeaving = () => {
      socket.emit("leave", game_id); 
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
    console.log(gameState)
  }
  ////

  return (
    <>
      <h1>Welcome to game {game_id}</h1>
      <ChatBox />
      <ShipPlacer />
      <h3>Development section</h3>
      <button onClick={handleClick}>print game state</button>
      <h3>{error}</h3>
      <WhereAmI />
    </>
  );
};

export default Game;
