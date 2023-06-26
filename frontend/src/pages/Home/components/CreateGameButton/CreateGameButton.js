import React, { useState } from "react";
import { createRoom } from "../../../../services/room";
import { useNavigate } from "react-router-dom";
import { socket } from "../../../../socket";

const CreateGameButton = () => {
  //TODO - forms to pick game configurations and save it as a state to send to server
  const gameconfigs = {
  size: 8,
  ships: [
    { Destroyer: 1 },
    { Cruiser: 2 },
    { Battleship: 0 },
    { AircraftCarrier: 1 }
  ],
  who_started: 1
}
;

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
