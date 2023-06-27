import React, { useContext } from "react";
import { Outlet, Navigate } from "react-router-dom";
import { LoggedInContext } from "../../App";

const PrivateRoutes = () => {
  const [loggedIn] = useContext(LoggedInContext);

  return loggedIn ? <Outlet /> : <Navigate to="/login" />;
};
export default PrivateRoutes;
