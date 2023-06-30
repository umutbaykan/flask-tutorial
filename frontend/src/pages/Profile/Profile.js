import React, { useEffect, useState } from "react";
import "./Profile.css";
import GamesPlayed from "./components/GamesPlayed/GamesPlayed";
import Statistics from "./components/Statistics/Statistics";

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
    <div className="profile-container">
      <GamesPlayed gamesHistory={gamesHistory} />
      <Statistics gamesHistory={gamesHistory} />
    </div>
  );
};

export default Profile;
