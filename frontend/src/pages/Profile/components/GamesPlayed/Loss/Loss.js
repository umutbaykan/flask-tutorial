import React from "react";
import propTypes from "prop-types";

const Loss = ({ game }) => {
  const { game_id, last_modified, players_info } = game;

  return (
    <div className="container game-history-ticket" key={game_id}>
      <p className="small-text">Game finished: {last_modified}</p>
      <p className="small-text">Players: </p>
      {players_info.map((player, index) => {
        return (
          <p className="small-text" key={`${game_id}-${index}`}>
            P{index + 1} - {player["username"]}
          </p>
        );
      })}
      <br></br>
      <p className="small-text error">Result: You lost.</p>
    </div>
  );
};

Loss.propTypes = { game: propTypes.object };

export default Loss;
