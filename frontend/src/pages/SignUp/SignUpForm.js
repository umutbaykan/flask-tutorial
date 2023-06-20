import React from "react";
import { Formik, Form } from "formik";
import TextField from "../../components/TextField/TextField";
import * as Yup from "yup";

const SignUpForm = () => {
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

  return (
    <Formik
      initialValues={{
        username: "",
        password: "",
        confirmPassword: "",
      }}
      validationSchema={validate}
      onSubmit={(values) => {
        console.log(values);
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
  );
};

export default SignUpForm;
