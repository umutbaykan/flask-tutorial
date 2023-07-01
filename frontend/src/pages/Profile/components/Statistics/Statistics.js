import React from "react";
import propTypes from "prop-types";
import { useCookies } from "react-cookie";

const Statistics = ({ gamesHistory }) => {
  const [cookies, ,] = useCookies(["user_id"]);

  let wins = 0;
  let loss = 0;
  let unfinished = 0;
  gamesHistory.forEach((game) => {
    if (game.who_won === cookies.user_id) {
      wins += 1;
    } else if (game.who_won === null) {
      unfinished += 1;
    } else {
      loss += 1;
    }
  });
  const total = wins + loss + unfinished;
  const winRatio = `${Math.round((wins / (total - unfinished)) * 100)}%`;

  return (
    <div className="container statistics">
      <h4>You have played:</h4>
      <p>A total of {total} games.</p>
      <p className="win">You won {wins} of them.</p>
      <p className="error">You lost {loss} of those.</p>
      <p>You did not finish {unfinished} games.</p>
      <p>For the games you finished, your win ratio is: {winRatio}</p>
    </div>
  );
};

Statistics.propTypes = { gamesHistory: propTypes.array };

export default Statistics;
