import React, { useState } from "react";
import propTypes from "prop-types";

import { joinRoom } from "../../../../services/room";
import { useNavigate } from "react-router-dom";
import { socket } from "../../../../socket";

export const JoinGameButton = ({ game_id }) => {
  JoinGameButton.propTypes = { game_id: propTypes.string };

  const navigate = useNavigate();
  const [error, setError] = useState("");

  const handleJoin = async () => {
    const result = await joinRoom(game_id);
    if (result.success) {
      socket.emit("join", game_id);
      navigate(`/game/${game_id}`);
    } else {
      setError(result.error);
    }
  };

  return (
    <>
      <button key={game_id} onClick={handleJoin}>
        {game_id}
      </button>
      <p>{error}</p>
    </>
  );
};

export default JoinGameButton;
