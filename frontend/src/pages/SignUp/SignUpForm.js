import React, { useState } from "react";
import { Formik, Form } from "formik";
import TextField from "../../components/TextField/TextField";
import * as Yup from "yup";
import { useNavigate } from "react-router-dom";

import { auth } from "../../services/auth";

const SignUpForm = () => {
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const validate = Yup.object({
    username: Yup.string()
      .min(3, "Must be at least 3 characters")
      .max(15, "Must be 15 characters or less")
      .required("Required"),
    password: Yup.string()
      .min(8, "Password must be at least 8 charaters")
      .required("Password is required"),
    confirmPassword: Yup.string()
      .oneOf([Yup.ref("password"), null], "Password must match")
      .required("Confirm password is required"),
  });

  const handleSubmit = async (values) => {
    const result = await auth(values.username, values.password, "register");
    if (result.success) {
      navigate("/");
    } else {
      setError(result.error);
      navigate("/signup");
    }
  };

  return (
    <>
      <Formik
        initialValues={{
          username: "",
          password: "",
          confirmPassword: "",
        }}
        validationSchema={validate}
        onSubmit={(values, { resetForm }) => {
          handleSubmit(values);
          resetForm();
        }}
      >
        {() => (
          <div>
            <h1>Sign Up</h1>
            <Form>
              <TextField label="username" name="username" type="text" />
              <TextField label="password" name="password" type="password" />
              <TextField
                label="Confirm Password"
                name="confirmPassword"
                type="password"
              />
              <button type="submit">Register</button>
            </Form>
          </div>
        )}
      </Formik>
      <p>{error}</p>
    </>
  );
};

export default SignUpForm;