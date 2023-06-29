import React, { useState, useContext } from "react";
import { createRoom } from "../../../../services/room";
import { useNavigate } from "react-router-dom";
import { socket } from "../../../../socket";

import GameConfigForm from "../GameConfigForm/GameConfigForm";

import { LoggedInContext } from "../../../../App";

// Remove import from below //
const gameConfigurations = require("../../../model_objects/game_simple_configs.json");
// REvemo import from above

const CreateGameButton = () => {
  //TODO - forms to pick game configurations and save it as a state to send to server
  const [loggedIn] = useContext(LoggedInContext);
  const gameconfigs = gameConfigurations;
  const navigate = useNavigate();
  const [error, setError] = useState("");

  const handleRoomCreation = async () => {
    if (!loggedIn) {
      navigate("/login");
    }
    const result = await createRoom(gameconfigs);
    if (result.room) {
      socket.emit("join", result.room);
      navigate(`/game/${result.room}`);
    } else {
      setError(result.error);
    }
  };

  return (
    <>
      <GameConfigForm handleSubmit={console.log}/>
      <button onClick={handleRoomCreation}>Create Game</button>
      <p>{error}</p>
    </>
  );
};

export default CreateGameButton;
