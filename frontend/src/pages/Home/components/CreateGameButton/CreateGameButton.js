import React, { useState } from "react";
import { createRoom } from "../../../../services/room";
import { useNavigate } from "react-router-dom";
import { socket } from "../../../../socket";

// Remove import from below //
const gameConfigurations = require("../../../model_objects/game_simple_configs.json");
// REvemo import from above

const CreateGameButton = () => {
  //TODO - forms to pick game configurations and save it as a state to send to server
  const gameconfigs = gameConfigurations
  const navigate = useNavigate();
  const [error, setError] = useState("");

  const handleRoomCreation = async () => {
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
      <button onClick={handleRoomCreation}>Create Game</button>
      <p>{error}</p>
    </>
  );
};

export default CreateGameButton;
