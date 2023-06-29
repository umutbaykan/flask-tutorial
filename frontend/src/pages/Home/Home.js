import React, { useContext } from "react";

import CurrentGames from "./components/CurrentGames/CurrentGames";
import GameConfigForm from "./components/GameConfigForm/GameConfigForm";

// TODO remove
import { auth } from "../../services/auth";
import { LoggedInContext } from "../../App";
import { useCookies } from "react-cookie";

const Home = () => {
  //// This section will be removed later
  const fastLogin = async () => {
    const result = await auth("Roger", "password", "login");
    setLoggedIn(true);
    removeCookie("user_id");
    setCookie("user_id", result.user_id);
  };

  const [, setCookie, removeCookie] = useCookies(["user_id"]);

  ///// This section will be removed later

  const [loggedIn, setLoggedIn] = useContext(LoggedInContext);

  return (
    <>
      <CurrentGames />
      {loggedIn && <GameConfigForm />}
      {/* Remove the button below */}
      <button onClick={fastLogin}>Fast Login</button>
      {/* Remove the button above */}
    </>
  );
};

export default Home;
