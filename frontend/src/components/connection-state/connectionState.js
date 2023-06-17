import React from "react";
import propTypes from 'prop-types';

export function ConnectionState({ isConnected }) {
  return <p>State: {"" + isConnected}</p>;
}

ConnectionState.propTypes = { isConnected: propTypes.bool}
