import React, {useState, useEffect, createContext} from "react";
import { Routes, Route } from "react-router-dom";
import { socket } from "./socket";

import Home from "./pages/Home/Home";
import Game from "./pages/Game/Game";
import SignUpForm from "./pages/SignUp/SignUpForm";
import LoginForm from "./pages/Login/LoginForm";
import NotFound from "./pages/NotFound/NotFound";
import Profile from "./pages/Profile/Profile";

export const LobbyContext = createContext({})
export const ChatContext = createContext([])

const App = () => {
  
  const [currentGames, setCurrentGames] = useState({});
  const [chats, setChats] = useState([])

  const onCurrentGames = (value) => {
    setCurrentGames((previous) => ({ ...previous, ...value }));
  }

  const onJoiningRoom = (value) => {
    setChats((previous) => [ ...previous, `${value.username} has joined the ${value.room}`])
  }

  const onLeavingRoom = (value) => {
    setChats((previous) => [ ...previous, `${value.username} has left the ${value.room}`])
  }

  // Event listeners
  useEffect(() => {
    socket.on("current_games", onCurrentGames);
    socket.on("user_joined", onJoiningRoom);
    socket.on("user_left", onLeavingRoom);
    return () => {
      socket.off("current_games", onCurrentGames);
      socket.off("user_joined", onJoiningRoom);
      socket.off('user_left', onLeavingRoom)
    };
  }, []);

  // Connection
  useEffect(() => {
    socket.connect();
    return () => {
      socket.disconnect();
    };
  }, [])

  return (
  <LobbyContext.Provider value={currentGames}>
  <ChatContext.Provider value={[chats, setChats]}>
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/signup" element={<SignUpForm />} />
      <Route path="/login" element={<LoginForm />} />
      <Route path="/game/:gameId" element={<Game />} />
      <Route path="/profile" element={<Profile />} />
      <Route path="*" element={<NotFound />} />
    </Routes>
  </ChatContext.Provider>
  </LobbyContext.Provider>
  );
};

export default App;
