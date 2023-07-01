import React, { useEffect, useState } from "react";
import "./Profile.css";
import GamesPlayed from "./components/GamesPlayed/GamesPlayed";
import Statistics from "./components/Statistics/Statistics";
import LoadGames from "./components/LoadGames/LoadGames";

import { getHistory } from "../../services/profile";
import { loadCheck } from "../../services/profile";

const Profile = () => {
  const [gamesHistory, setGamesHistory] = useState([]);
  const [loadHistory, setLoadHistory] = useState({});

  const getAllGamesOfUser = async () => {
    const result = await getHistory();
    setGamesHistory(result);
  };

  const getAllLoadRequests = async () => {
    const result = await loadCheck();
    setLoadHistory(result);
  };

  useEffect(() => {
    getAllGamesOfUser();
    getAllLoadRequests();
  }, []);

  if (gamesHistory === []) {
    return;
  }

  return (
    <div className="container">
      <GamesPlayed gamesHistory={gamesHistory} />
      <div className="container profile">
        <Statistics gamesHistory={gamesHistory} />
        <LoadGames loadHistory={loadHistory} />
      </div>
    </div>
  );
};

export default Profile;
