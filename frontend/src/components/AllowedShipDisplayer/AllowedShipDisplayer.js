import React from 'react';
import propTypes from "prop-types"

const AllowedShipDisplayer = ({ allowedShips }) => {

    return (
        <>
          {Object.entries(allowedShips).map(([ship, quantity]) => (
            <ul className='small-text' key={ship}>
              {ship} - {quantity}
            </ul>
          ))}
        </>
    )
}

AllowedShipDisplayer.propTypes = { allowedShips: propTypes.object }

export default AllowedShipDisplayer