import React from "react";
import propTypes from "prop-types";

const GameEnd = ({ didIwin }) => {
  const youWon = didIwin ? true : false
  if (youWon) {
    return <h1>Congratulations, you win!</h1>
  } else {
    return <h1>Unlucky! Hopefully next time!</h1>
  }
};

GameEnd.propTypes = { didIwin: propTypes.bool };

export default GameEnd;
