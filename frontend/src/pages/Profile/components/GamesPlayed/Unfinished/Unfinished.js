import React from "react";
import propTypes from "prop-types";
import { useCookies } from "react-cookie";
import JoinGameButton from "../../../../../components/JoinGameButton/JoinGameButton";
import AllowedShipDisplayer from "../../../../../components/AllowedShipDisplayer/AllowedShipDisplayer";

import { whoseTurnIsIt } from "../../../../../utils/turn";

const Unfinished = ({ game }) => {
  const { game_id, last_modified, players_info, allowed_ships } = game;
  const [cookies, ,] = useCookies(["user_id"]);

  return (
    <div className="container game-history-ticket" key={game_id}>
      <p className="small-text">Last move: {last_modified}</p>
      <p className="small-text">Players: </p>
      {players_info.map((player, index) => {
        return (
          <p className="small-text" key={`${game_id}-${index}`}>
            P{index + 1} - {player["username"]}
          </p>
        );
      })}
      <br></br>
      <p className="small-text">Ships:</p>
      <AllowedShipDisplayer allowedShips={allowed_ships} />
      <p className="small-text">
        {whoseTurnIsIt(game, cookies.user_id)} turn next.
      </p>
      <br></br>
      <p className="small-text">Unfinished game. Click button below to load.</p>
      <p className="small-text">
        Your opponent will get a notifier on their profile page.
      </p>
      <JoinGameButton game_id={game_id} load={true} />
    </div>
  );
};

Unfinished.propTypes = { game: propTypes.object };

export default Unfinished;
