import React from "react";
import propTypes from "prop-types";

const Win = ({ winner }) => {
  return <h1>Hooray, {winner} won!</h1>;
};

Win.propTypes = { winner: propTypes.string };

export default Win;
