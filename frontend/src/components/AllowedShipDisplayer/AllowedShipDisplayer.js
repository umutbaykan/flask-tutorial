import React from 'react';
import propTypes from "prop-types"

const AllowedShipDisplayer = ({ allowedShips }) => {

    return (
        <div className='allowed-ship-container'>
        <h1>Allowed Ships</h1>
        <ul>
          {Object.entries(allowedShips).map(([ship, quantity]) => (
            <ul key={ship}>
              {ship} - {quantity}
            </ul>
          ))}
        </ul>
        </div>
    )
}

AllowedShipDisplayer.propTypes = { allowedShips: propTypes.object }

export default AllowedShipDisplayer