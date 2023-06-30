import React from "react";
import propTypes from "prop-types";
import "./Statistics.css";
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
    <div className="statistics-container">
      <h1>You have played:</h1>
      <h3>A total of {total} games.</h3>
      <h3>You won {wins} of them.</h3>
      <h3>You lost {loss} of those.</h3>
      <h3>You did not finish {unfinished} games.</h3>
      <h3>For the games you finished, your win ratio is: {winRatio}</h3>
    </div>
  );
};

Statistics.propTypes = { gamesHistory: propTypes.array };

export default Statistics;
