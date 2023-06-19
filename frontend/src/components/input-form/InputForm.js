import React, { useState } from "react";
import propTypes from 'prop-types';

export function InputForm({callback, buttonValue}) {
  const [value, setValue] = useState(null);

  const handleSubmit = () => {
    event.preventDefault();
    callback(value)
  }

  return (
    <form onSubmit={handleSubmit}>
      <input onChange={(e) => setValue(e.target.value)} />
      <button type="submit">
        {buttonValue}
      </button>
    </form>
  );
}

InputForm.propTypes = { callback: propTypes.func, buttonValue: propTypes.string}
