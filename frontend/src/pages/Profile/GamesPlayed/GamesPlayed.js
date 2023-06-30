import React, { useEffect, useState } from "react";
import { useCookies } from "react-cookie";

import Won from "../Won/Won";
import Loss from "../Loss/Loss";
import Unfinished from "../Unfinished/Unfinished";

import { getHistory } from "../../../services/profile";

const GamesPlayed = () => {
  const [gamesHistory, setGamesHistory] = useState([]);
  const [cookies, ,] = useCookies(["user_id"]);

  const getAllGamesOfUser = async () => {
    const result = await getHistory();
    setGamesHistory(result);
  };

  const parseGame = (game) => {
    const { who_won, game_id } = game;
    let result;
    if (who_won === cookies.user_id) {
      result = <Won key={game_id} game={game} />;
    } else if (who_won === null) {
      result = <Unfinished key={game_id} game={game} />;
    } else {
      result = <Loss key={game_id} game={game} />;
    }
    return result;
  };

  useEffect(() => {
    getAllGamesOfUser();
  }, []);

  return (
    <>
      <h3>Your games so far:</h3>
      {gamesHistory.map((game) => {
        return parseGame(game);
      })}
    </>
  );
};

export default GamesPlayed;
