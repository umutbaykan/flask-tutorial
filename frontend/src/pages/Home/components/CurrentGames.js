import React, { useEffect, useState } from "react";
import { socket } from "../../../socket";

export const CurrentGames = () => {
  const [currentGames, setCurrentGames] = useState({});

  function onCurrentGames(value) {
    setCurrentGames((previous) => ({ ...previous, ...value }));
  }

  useEffect(() => {
    socket.connect();
    socket.on("current_games", onCurrentGames);

    return () => {
      socket.disconnect();
      socket.off("current_games", onCurrentGames);
    };
  }, []);
  return (
    <>
      <h3>Current available games:</h3>
      <div>
        {Object.keys(currentGames).map((key) => (
          <p key={key}>
            {key}: {currentGames[key].gamestate}
          </p>
        ))}
      </div>
    </>
  );
};

export default CurrentGames;
