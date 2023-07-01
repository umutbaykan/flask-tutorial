import React from "react";
import propTypes from "prop-types";
import { useCookies } from "react-cookie";
import JoinGameButton from "../../../../components/JoinGameButton/JoinGameButton";

import { whoseTurnIsIt } from "../../../../utils/turn";

const LoadGames = ({ loadHistory }) => {
  const [cookies, ,] = useCookies(["user_id"]);

  if (!loadHistory) {
    return;
  }

  const generateButtons = () => {
    return Object.entries(loadHistory).map(([game_id, value]) => (
      <div key={game_id}>
        <p>Last Modified: {value.last_modified}</p>
        <p>{whoseTurnIsIt(value, cookies.user_id)} plays next.</p>
        <JoinGameButton game_id={game_id} load={true} />
      </div>
    ));
  };

  return <>{generateButtons()}</>;
};

LoadGames.propTypes = { loadHistory: propTypes.object };

export default LoadGames;
