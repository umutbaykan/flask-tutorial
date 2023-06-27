import React, { useState, useEffect, useContext } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { socket } from "../../socket";

import { GameStateContext } from "../../App";
import { ChatContext } from "../../App";

import WhereAmI from "../../components/whereami/whereami";
import ChatBox from "./components/ChatBox/ChatBox";

const Game = () => {
  const { pathname } = useLocation();
  const [game_id] = useState(pathname.substring(pathname.lastIndexOf("/") + 1));
  const [ , setChats] = useContext(ChatContext);
  const [gameState, setGameState] = useContext(GameStateContext);

  const navigate = useNavigate();

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
      {/* <h3>{roomInfo}</h3> */}
      <ChatBox />
      <br></br>
      <button
        onClick={() => {
          navigate("/");
        }}
      >
        Leave game and go back to lobby
      </button>
      <button onClick={handleClick}>print game state</button>
      <WhereAmI />
    </>
  );
};

export default Game;
