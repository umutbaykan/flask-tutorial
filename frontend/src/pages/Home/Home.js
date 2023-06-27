import React, { useContext } from "react";

import NavButton from "../../components/NavButton/NavButton";
import CurrentGames from "./components/CurrentGames/CurrentGames";
import CreateGameButton from "./components/CreateGameButton/CreateGameButton";

// TODO remove
import { auth, logout } from "../../services/auth";
import { LoggedInContext } from "../../App";
import WhereAmI from "../../components/whereami/whereami"

const Home = () => {
  //// This section will be removed later
  const fastLogin = async () => {
    await auth("Roger", "password", "login");
    setLoggedIn(true)
  };

  const handleLogout = async () => {
    await logout();
    setLoggedIn(false)
  };

  const [loggedIn, setLoggedIn] = useContext(LoggedInContext)
  ///// This section will be removed later

  return (
    <>
      <h1>welcome home</h1>
      <h5>You are currently logged {loggedIn ? <h5>in</h5> : <h5>out</h5>}</h5>
      <CurrentGames />
      <div>
        <NavButton to={"/signup"} text={"Sign Up"} />
        <br></br>
        <NavButton to={"/login"} text={"Login"} />
        <br></br>
        <NavButton to={"/profile"} text={"Profile"} />
        <br></br>
        <button onClick={handleLogout}>Logout</button>
      </div>
      <CreateGameButton />
      {/* Remove the button below */}
      <button onClick={fastLogin}>Fast Login</button>
      {/* Remove the button above */}
      <WhereAmI />
    </>
  );
};

export default Home;
