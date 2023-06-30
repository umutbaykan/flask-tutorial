import React, { useEffect, useState } from "react";
import GamesPlayed from "./components/GamesPlayed/GamesPlayed";

import { getHistory } from "../../services/profile";

const Profile = () => {
  const [gamesHistory, setGamesHistory] = useState([]);

  const getAllGamesOfUser = async () => {
    const result = await getHistory();
    setGamesHistory(result);
  };

  useEffect(() => {
    getAllGamesOfUser();
  }, []);

  if (gamesHistory === []) {
    return;
  }

  return (
    <div>
      <GamesPlayed gamesHistory={gamesHistory} />
    </div>
  );
};

export default Profile;
