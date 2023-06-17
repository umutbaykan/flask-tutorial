import React from "react";
import propTypes from 'prop-types';

export function Events({ events }) {
  return (
    <ul>
      {events.map((event, index) => (
        <li key={index}>{event}</li>
      ))}
    </ul>
  );
}

Events.propTypes = { events: propTypes.array}

