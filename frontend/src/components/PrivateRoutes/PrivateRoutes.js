import React from "react";
import { Outlet, Navigate } from "react-router-dom";
import { useCookies } from "react-cookie";

const PrivateRoutes = () => {
  const [cookie] = useCookies(["user_id"]);

  return cookie.user_id ? <Outlet /> : <Navigate to="/login" />;
};
export default PrivateRoutes;
