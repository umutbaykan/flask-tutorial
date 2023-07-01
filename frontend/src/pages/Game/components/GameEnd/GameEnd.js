import React from "react";
import propTypes from "prop-types";

const GameEnd = ({ didIwin }) => {
  const youWon = didIwin ? true : false;
  if (youWon) {
    return <h4>Congratulations captain, you win!</h4>;
  } else {
    return <h4>All your ships have sunk, you lost captain!</h4>;
  }
};

GameEnd.propTypes = { didIwin: propTypes.bool };

export default GameEnd;
