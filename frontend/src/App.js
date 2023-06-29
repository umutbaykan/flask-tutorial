import React, { useState, useEffect, createContext } from "react";
import { Routes, Route } from "react-router-dom";
import { socket } from "./socket";
import { useCookies } from "react-cookie";

import Home from "./pages/Home/Home";
import Game from "./pages/Game/Game";
import SignUpForm from "./pages/SignUp/SignUpForm";
import LoginForm from "./pages/Login/LoginForm";
import NotFound from "./pages/NotFound/NotFound";
import Profile from "./pages/Profile/Profile";
import PublicRoutes from "./components/PublicRoutes/PublicRoutes";
import PrivateRoutes from "./components/PrivateRoutes/PrivateRoutes";
import NavBar from "./components/NavBar/NavBar";

export const LobbyContext = createContext({});
export const ChatContext = createContext([]);
export const LoggedInContext = createContext();
export const GameStateContext = createContext();
export const ErrorContext = createContext();

const App = () => {
  const [currentGames, setCurrentGames] = useState({});
  const [chats, setChats] = useState([]);
  const [gameState, setGameState] = useState();
  const [loggedIn, setLoggedIn] = useState(false);
  const [error, setError] = useState("")
  const [cookies, ,] = useCookies(["user_id"]);

  const onCurrentGames = (games) => {
    setCurrentGames((previous) => {
      const updatedGames = { ...previous, ...games };
      for (const gameId in previous) {
        if (!(gameId in games)) {
          delete updatedGames[gameId];
        }
      }

      return updatedGames;
    });
  };

  const onJoiningRoom = (data) => {
    setChats((previous) => [
      ...previous,
      `${data.username} has joined ${data.room}`,
    ]);
  };

  const onLeavingRoom = (user) => {
    setChats((previous) => [
      ...previous,
      `${user.username} has left ${user.room}`,
    ]);
  };

  const onChatUpdate = (chat) => {
    setChats((previous) => [...previous, `${chat.username}: ${chat.message}`]);
  };

  const onGameUpdate = (data) => {
    setError("")
    setGameState(() => data.game)
  }

  const onError = (data) => {
    setError(() => data.error)
  }

  // Event listeners
  useEffect(() => {
    socket.on("current_games", onCurrentGames);
    socket.on("user_joined", onJoiningRoom);
    socket.on("user_left", onLeavingRoom);
    socket.on("chat_update", onChatUpdate);
    socket.on("update", onGameUpdate)
    socket.on("error", onError)
    return () => {
      socket.off("current_games", onCurrentGames);
      socket.off("user_joined", onJoiningRoom);
      socket.off("user_left", onLeavingRoom);
      socket.off("chat_update", onChatUpdate);
      socket.off("update", onGameUpdate)
      socket.off("error", onError)
    };
  }, []);

  // Connection
  useEffect(() => {
    socket.connect();
    return () => {
      socket.disconnect();
    };
  }, [loggedIn]);

  // Authenticate whether you are already logged in
  useEffect(() => {
    if (cookies.user_id) {
      setLoggedIn(true);
    } else {
      setLoggedIn(false);
    }
  }, []);

  return (
    <LobbyContext.Provider value={currentGames}>
      <LoggedInContext.Provider value={[loggedIn, setLoggedIn]}>
        <ChatContext.Provider value={[chats, setChats]}>
          <GameStateContext.Provider value={[gameState, setGameState]}>
            <ErrorContext.Provider value={[error, setError]}>
              <NavBar />
              <Routes>
                <Route element={<PublicRoutes />}>
                  <Route path="/signup" element={<SignUpForm />} />
                  <Route path="/login" element={<LoginForm />} />
                </Route>
                <Route element={<PrivateRoutes />}>
                  <Route path="/profile" element={<Profile />} />
                  <Route path="/game/:gameId" element={<Game />} />
                </Route>
                <Route path="/" element={<Home />} />
                <Route path="*" element={<NotFound />} />
              </Routes>
            </ErrorContext.Provider>
          </GameStateContext.Provider>
        </ChatContext.Provider>
      </LoggedInContext.Provider>
    </LobbyContext.Provider>
  );
};

export default App;
