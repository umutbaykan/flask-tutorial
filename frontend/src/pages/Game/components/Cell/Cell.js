import "./Cell.css";
import propTypes from "prop-types";
import React from "react";

const Cell = ({ coordinates, display, type, action }) => {
  const handleCellPress = () => {
    action(coordinates);
  };

  return (
    <button onClick={handleCellPress} className={`cell cell-${type}`}>
      {display}
    </button>
  );
};

Cell.propTypes = {
  coordinates: propTypes.array,
  display: propTypes.string,
  type: propTypes.string,
  action: propTypes.func,
};

export default Cell;
