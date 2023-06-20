import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';

const Game = () => {
  const { pathname } = useLocation();
  const [game_id] = useState(pathname.substring(pathname.lastIndexOf("/") + 1));

  return (
    <h1>Welcome to game {game_id}</h1>
  );
};

export default Game