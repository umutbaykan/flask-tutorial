import React, { useState } from "react";
import { createRoom } from "../../../../services/room";
import { useNavigate } from "react-router-dom";
import { socket } from "../../../../socket";

const CreateGameButton = () => {
  //TODO - forms to pick game configurations and save it as a state to send to server
  const gameconfigs = { arraySize: 10, ships: ["1", "2", "3"] };

  const navigate = useNavigate();
  const [error, setError] = useState("");

  const handleRoomCreation = async () => {
    const result = await createRoom(gameconfigs);
    if (result.room) {
      socket.emit("join");
      navigate(`/game/${result.room}`);
    } else {
      setError(result.error);
      navigate("/");
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
