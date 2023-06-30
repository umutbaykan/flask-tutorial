import React from "react";
import "../GamesPlayed.css";
import propTypes from "prop-types";
import { useCookies } from "react-cookie";

import { whoseTurnIsIt } from "../../../../../utils/turn";

const Unfinished = ({ game }) => {
  const { game_id, last_modified, players_info, allowed_ships } = game;
  const [cookies, ,] = useCookies(["user_id"]);

  return (
    <div className="container unfinished" key={game_id}>
      <p>Last move: {last_modified}</p>
      <p>Players: </p>
      {players_info.map((player, index) => {
        return (
          <p key={`${game_id}-${index}`}>
            P{index + 1} - {player["username"]}
          </p>
        );
      })}
      <p>Ships:</p>
      {Object.entries(allowed_ships).map(([ship, quantity]) => (
        <ul key={ship}>
          {ship} - {quantity}
        </ul>
      ))}
      <p>{whoseTurnIsIt(game, cookies.user_id)} plays next.</p>
      <p>Unfinished game</p>
      <button onClick={console.log("one day")}>Load</button>
    </div>
  );
};

Unfinished.propTypes = { game: propTypes.object };

export default Unfinished;
