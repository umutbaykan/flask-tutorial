import React, { useState, useEffect } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { socket } from "../../socket";

import WhereAmI from "../../components/whereami/whereami"


const Game = () => {
  const { pathname } = useLocation();
  const [game_id] = useState(pathname.substring(pathname.lastIndexOf("/") + 1));
  const navigate = useNavigate();

  // const [roomInfo, setRoomInfo] = useState("");

  // useEffect(() => {
  //   function onRoomInfo(value) {
  //     setRoomInfo(() => value);
  //   }

  //   socket.emit("roomevent", () => {});

  //   socket.on("join-room", onRoomInfo);

  //   return () => {
  //     socket.off("join-room", onRoomInfo);
  //   };
  // }, []);


  useEffect(() => {
    const handleUserLeaving = () => {
      socket.emit('leave', game_id); // Replace with your desired socket event name
    };

    window.addEventListener('beforeunload', handleUserLeaving);

    return () => {
      window.removeEventListener('beforeunload', handleUserLeaving);
      handleUserLeaving();
    };
  }, []);

  return (
    <>
      <h1>Welcome to game {game_id}</h1>
      {/* <h3>{roomInfo}</h3> */}

      <br></br>
      <button onClick={() => {navigate('/')}}>Leave game and go back to lobby</button>
      <WhereAmI />
    </>
  );
};

export default Game;
