import React from "react";
import propTypes from "prop-types";
import JoinGameButton from "../../../Home/components/JoinGameButton/JoinGameButton";

const LoadGames = ({ loadHistory }) => {
  if (!loadHistory) {
    return;
  }

  const generateButtons = () => {
    const buttons = [];
    for (let game in loadHistory) {
      buttons.push(<JoinGameButton game_id={game} load={true} />);
    }
    return buttons;
  };

  return <>{generateButtons()}</>;
};

LoadGames.propTypes = { loadHistory: propTypes.object };

export default LoadGames;
