import React, { useState, useContext } from "react";
import { Formik, Form, Field } from "formik";
import NumberField from "../../../../components/NumberField/NumberField";
import * as Yup from "yup";
import { useNavigate } from "react-router-dom";

import { socket } from "../../../../socket";
import { createRoom } from "../../../../services/room";
import { LoggedInContext } from "../../../../App";


const GameConfigForm = () => {
    const [loggedIn] = useContext(LoggedInContext);
    const navigate = useNavigate();
    const [error, setError] = useState("");

  const validate = Yup.object({
    size: Yup.number()
      .min(5, "Must be at least 5")
      .max(16, "Must be 16 or less"),
    destroyer: Yup.number()
      .min(0, "Cant have negative ships")
      .max(5, "Lets not go crazy captain"),
    cruiser: Yup.number()
      .min(0, "Cant have negative ships")
      .max(5, "Lets not go crazy captain"),
    battleship: Yup.number()
      .min(0, "Cant have negative ships")
      .max(5, "Lets not go crazy captain"),
    aircraftCarrier: Yup.number()
      .min(0, "Cant have negative ships")
      .max(5, "Lets not go crazy captain")
  });

  const handleSubmit = async (gameconfigs) => {
    if (!loggedIn) {
      navigate("/login");
    }
    const result = await createRoom(gameconfigs
      );
    if (result.room) {
      socket.emit("join", result.room);
      navigate(`/game/${result.room}`);
    } else {
      setError(result.error);
    }
  };

  return (
    <>
      <Formik
        initialValues={{
          size: 5,
          destroyer: 1,
          cruiser: 0,
          battleship: 0,
          aircraftCarrier: 0,
          who_started: 0,
        }}
        validationSchema={validate}
        onSubmit={(values) => {
          const {
            size,
            destroyer,
            cruiser,
            battleship,
            aircraftCarrier,
            who_started,
          } = values;
          const formattedValues = {
            size,
            ships: [
              {Destroyer: destroyer},
              {Cruiser: cruiser},
              {Battleship: battleship},
              {AircraftCarrier: aircraftCarrier},
            ],
            who_started: parseInt(who_started),
          };
          handleSubmit(formattedValues);
        }}
      >
        {() => (
          <div>
            <h1>Lets configure your game!</h1>
            <Form>
              <h3>Choose your board size</h3>
              <NumberField label="size" name="size" />
              <h3>Now lets pick your ships</h3>
              <NumberField label="Destroyer" name="destroyer" />
              <NumberField label="Cruiser" name="cruiser" />
              <NumberField label="Battleship" name="battleship" />
              <NumberField label="Aircraft Carrier" name="aircraftCarrier" type="number"/>
              <h3>
                Who do you want to start? You will be player 1 if you create the
                game.
              </h3>
              <label>
                <Field type="radio" name="who_started" value="0" />
                One
              </label>
              <label>
                <Field type="radio" name="who_started" value="1" />
                Two
              </label>
              <button type="submit">Create game</button>
            </Form>
          </div>
        )}
      </Formik>
      <p>{error}</p>
    </>
  );
};

export default GameConfigForm;
