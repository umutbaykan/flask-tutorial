import React from "react";
import "../GamesPlayed.css";
import propTypes from "prop-types";

const Won = ({ game }) => {
  const { game_id, last_modified, players_info } = game;

  return (
    <div className="container win" key={game_id}>
      <p>Game finished: {last_modified}</p>
      <p>Players: </p>
      {players_info.map((player, index) => {
        return (
          <p key={`${game_id}-${index}`}>
            P{index + 1} - {player["username"]}
          </p>
        );
      })}
      <p>Result: You won.</p>
    </div>
  );
};

Won.propTypes = { game: propTypes.object };

export default Won;
