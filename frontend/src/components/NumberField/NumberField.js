import React from 'react';
import "./NumberField.css"
import propTypes from 'prop-types';
import { ErrorMessage, useField } from 'formik';

const NumberField = ({ label, ...props }) => {
  const [field, meta] = useField(props);
  return (
    <div className="number-field">
      <label htmlFor={field.name}>{label}</label>
      <input
        id={field.name} className={`form-control shadow-none ${meta.touched && meta.error && 'is-invalid'}`}
        {...field} {...props}
        autoComplete="off"
        type="number"
      />
      <ErrorMessage component="div" name={field.name} className="small-text error" />
    </div>
  )
}

NumberField.propTypes = { label: propTypes.string}


export default NumberField;