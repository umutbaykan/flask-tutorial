import React, {useState, useEffect, createContext} from "react";
import { useNavigate, Routes, Route } from "react-router-dom";
import { socket } from "./socket";

import Home from "./pages/Home/Home";
import Game from "./pages/Game/Game";
import SignUpForm from "./pages/SignUp/SignUpForm";
import LoginForm from "./pages/Login/LoginForm";
import NotFound from "./pages/NotFound/NotFound";

export const LobbyContext = createContext({})

const App = () => {
  
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
  <LobbyContext.Provider value={currentGames}>
    <Routes>
      <Route path="/" element={<Home navigate={useNavigate()} />} />
      <Route path="/signup" element={<SignUpForm navigate={useNavigate()} />} />
      <Route path="/login" element={<LoginForm navigate={useNavigate()} />} />
      <Route path="/game/:gameId" element={<Game />} />
      <Route path="*" element={<NotFound />} />
    </Routes>
  </LobbyContext.Provider>
  );
};

export default App;
