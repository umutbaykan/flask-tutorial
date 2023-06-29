import "./ChatForm.css";
import { React, useContext } from "react";
import { Formik, Form } from "formik";
import * as Yup from "yup";

import TextField from "../../../../components/TextField/TextField";

import { GameStateContext } from "../../../../App";
import { socket } from "../../../../socket";

const ChatForm = () => {
  const [gameState] = useContext(GameStateContext);

  const validate = Yup.object({
    chat: Yup.string().required(""),
  });

  const handleSubmit = (message) => {
    socket.emit("chat", { message: message.chat, room: gameState.game_id });
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
          <>
            <Form>
              <div className="form-row">
                <TextField name="chat" type="text" />
                <button type="submit">Send</button>
              </div>
            </Form>
          </>
        )}
      </Formik>
    </>
  );
};

export default ChatForm;
