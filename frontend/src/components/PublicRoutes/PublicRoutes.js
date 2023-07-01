import React from "react";
import { Outlet, Navigate } from "react-router-dom";
import { useCookies } from "react-cookie";

const PublicRoutes = () => {
  const [cookie] = useCookies(["user_id"]);

  return cookie.user_id ? <Navigate to="/" /> : <Outlet />;
};
export default PublicRoutes;
