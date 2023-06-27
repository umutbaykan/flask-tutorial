import { React, useState } from "react";
import { Formik, Form } from "formik";
import { useLocation } from "react-router-dom";
import * as Yup from "yup";

import TextField from "../../../../components/TextField/TextField";

import { socket } from "../../../../socket";

const ChatForm = () => {
  const { pathname } = useLocation();
  const [game_id] = useState(pathname.substring(pathname.lastIndexOf("/") + 1));

  const validate = Yup.object({
    chat: Yup.string().required(""),
  });

  const handleSubmit = (message) => {
    socket.emit("chat", { message: message.chat, room: game_id });
  };

  return (
    <>
      <Formik
        initialValues={{
          chat: "",
        }}
        validationSchema={validate}
        onSubmit={(values, { resetForm }) => {
          handleSubmit(values);
          resetForm();
        }}
      >
        {() => (
          <div>
            <h5>Chat here:</h5>
            <Form>
              <TextField label="chat" name="chat" type="text" />
              <button type="submit">Send</button>
            </Form>
          </div>
        )}
      </Formik>
    </>
  );
};

export default ChatForm;
