import React, { useState } from "react";
import { Formik, Form } from "formik";
import TextField from "../../components/TextField/TextField";
import * as Yup from "yup";
import { useNavigate } from "react-router-dom";

import { auth } from "../../services/auth";

const LoginForm = () => {
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const validate = Yup.object({
    username: Yup.string().required("Required"),
    password: Yup.string().required("Password is required"),
  });

  const handleSubmit = async (values) => {
    const result = await auth(values.username, values.password, "login");
    if (result.success) {
      navigate("/");
    } else {
      setError(result.error);
      navigate("/login");
    }
  };

  return (
    <>
      <Formik
        initialValues={{
          username: "",
          password: "",
        }}
        validationSchema={validate}
        onSubmit={(values, { resetForm }) => {
          handleSubmit(values);
          resetForm();
        }}
      >
        {() => (
          <div>
            <h1>Log In</h1>
            <Form>
              <TextField label="username" name="username" type="text" />
              <TextField label="password" name="password" type="password" />
              <button type="submit">Login</button>
            </Form>
          </div>
        )}
      </Formik>
      <p>{error}</p>
    </>
  );
};

export default LoginForm;
