import './Cell.css'
import React from 'react';

const Cell = ({coordinates}) => {

    const handleCellPress = () => {
        console.log(coordinates)
      }

    return (
        <button onClick={handleCellPress} className='cell'>O</button>
        )
}

export default Cell

