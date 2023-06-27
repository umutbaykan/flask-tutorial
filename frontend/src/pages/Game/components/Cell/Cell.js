import './Cell.css'
import propTypes from 'prop-types';
import React from 'react';

const Cell = ({coordinates, display, type}) => {

    const handleCellPress = () => {
        console.log(coordinates)
      }

    return (
        <button onClick={handleCellPress} className={`cell cell-${type}`}>{display}</button>
        )
}

Cell.propTypes = { coordinates: propTypes.string, display: propTypes.string, type: propTypes.string}


export default Cell

