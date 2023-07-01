import React from "react";
import "./AllowedShipDisplayer.css";
import propTypes from "prop-types";

const AllowedShipDisplayer = ({ allowedShips }) => {
  return (
    <div className="allowed-ships">
      {Object.entries(allowedShips).map(([ship, quantity]) => (
        <p className="small-text" key={ship}>
          {ship} - {quantity}
        </p>
      ))}
    </div>
  );
};

AllowedShipDisplayer.propTypes = { allowedShips: propTypes.object };

export default AllowedShipDisplayer;
