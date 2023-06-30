import React, { useState } from "react";
import propTypes from "prop-types";

import { joinRoom } from "../../../../services/room";
import { useNavigate } from "react-router-dom";
import { socket } from "../../../../socket";

export const JoinGameButton = ({ game_id, load }) => {
  const navigate = useNavigate();
  const [error, setError] = useState("");

  const handleJoin = async () => {
    let result;
    load ? result = {success: true} : result = await joinRoom(game_id);
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

JoinGameButton.propTypes = { game_id: propTypes.string, load: propTypes.bool };

export default JoinGameButton;
