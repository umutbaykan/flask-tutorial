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
      <div className="container load-item" key={game_id}>
        <p className="small-text">Last Modified: {value.last_modified}</p>
        <p className="small-text">
          {whoseTurnIsIt(value, cookies.user_id)} turn next.
        </p>
        <JoinGameButton game_id={game_id} load={true} />
      </div>
    ));
  };

  let results = generateButtons();
  if (results.length === 0) {
    results = (
      <p className="small-text error">
        You have no requests to join any loaded games at this moment.
      </p>
    );
  }

  return (
    <div className="container load-requests">
      <h4>Your active load requests display here:</h4>
      <br></br>
      {results}
    </div>
  );
};

LoadGames.propTypes = { loadHistory: propTypes.object };

export default LoadGames;
