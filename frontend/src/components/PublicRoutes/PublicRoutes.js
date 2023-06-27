import React, { useContext } from "react";
import { Outlet, Navigate } from "react-router-dom";
import { LoggedInContext } from "../../App";

const PublicRoutes = () => {
  const [loggedIn] = useContext(LoggedInContext);

  return loggedIn ? <Navigate to="/" /> : <Outlet />;
};
export default PublicRoutes;
