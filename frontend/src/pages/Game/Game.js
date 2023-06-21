import React, { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import { socket } from "../../socket";

import { ConnectionManager } from "../../components/ConnectionManager/ConnectionManager";
import { ConnectionState } from "../../components/ConnectionState/ConnectionState";
import NavButton from "../../components/NavButton/NavButton";

const Game = () => {
  const { pathname } = useLocation();
  const [game_id] = useState(pathname.substring(pathname.lastIndexOf("/") + 1));
  const [isConnected] = useState(socket.connected);
  const [roomInfo, setRoomInfo] = useState("");

  useEffect(() => {
    function onRoomInfo(value) {
      setRoomInfo(() => value);
    }

    socket.emit("roomevent", () => {});

    socket.on("join-room", onRoomInfo);

    return () => {
      socket.off("join-room", onRoomInfo);
    };
  }, []);

  return (
    <>
      <h1>Welcome to game {game_id}</h1>
      <h3>{roomInfo}</h3>
      <ConnectionState isConnected={isConnected} />
      <ConnectionManager />
      <br></br>
      <NavButton to={"/"} text={"Go home"} />
    </>
  );
};

export default Game;
