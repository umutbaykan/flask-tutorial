import "./NavBar.css";
import React, { useContext } from "react";
import { useCookies } from "react-cookie";
import { NavLink } from "react-router-dom";

import { logout } from "../../services/auth";
import { LoggedInContext } from "../../App";

const NavBar = () => {
  const [loggedIn, setLoggedIn] = useContext(LoggedInContext);
  const [, , removeCookie] = useCookies(["user_id"]);

  const handleLogout = async () => {
    await logout();
    removeCookie("user_id");
    setLoggedIn(false);
  };

  return (
    <div className="topnav">
      <NavLink to={"/"} className={"battleships-link"}>
        Battleships
      </NavLink>
      {loggedIn ? (
        <div className="topnav-container">
          <button className="topnav-button" onClick={handleLogout}>
            Logout
          </button>
          <NavLink to={"/profile"}>Profile</NavLink>
        </div>
      ) : (
        <div className="topnav-container">
          <NavLink to={"/signup"}>Sign Up</NavLink>
          <NavLink to={"/login"}>Login</NavLink>
        </div>
      )}
    </div>
  );
};

export default NavBar;
