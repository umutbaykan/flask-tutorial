export const whoseTurnIsIt = (gameState, user_id) => {
    return (gameState.players.indexOf(user_id) +
      gameState.turn +
      gameState.who_started) %
      2 ===
      0
      ? "Your"
      : "Opponent";
  };