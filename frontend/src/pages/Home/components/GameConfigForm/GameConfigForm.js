import React, { useState } from "react";
import propTypes from "prop-types";
import { Formik, Form, Field } from "formik";
import NumberField from "../../../../components/NumberField/NumberField";
import * as Yup from "yup";

const GameConfigForm = ({ handleSubmit }) => {
  const [error] = useState("");

  const validate = Yup.object({
    size: Yup.number()
      .min(5, "Must be at least 5")
      .max(16, "Must be 16 or less"),
    Destroyer: Yup.number()
      .min(0, "Cant have negative ships")
      .max(5, "Lets not go crazy captain"),
    Cruiser: Yup.number()
      .min(0, "Cant have negative ships")
      .max(5, "Lets not go crazy captain"),
    Battleship: Yup.number()
      .min(0, "Cant have negative ships")
      .max(5, "Lets not go crazy captain"),
    AircraftCarrier: Yup.number()
      .min(0, "Cant have negative ships")
      .max(5, "Lets not go crazy captain"),
  });

  return (
    <>
      <Formik
        initialValues={{
          size: 10,
          destroyer: 1,
          cruiser: 1,
          battleship: 1,
          aircraftCarrier: 1,
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
            ships: {
              Destroyer: destroyer,
              Cruiser: cruiser,
              Battleship: battleship,
              AircraftCarrier: aircraftCarrier,
            },
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
              <NumberField label="Aircraft Carrier" name="aircraftCarrier" />
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

GameConfigForm.propTypes = { handleSubmit: propTypes.func };

export default GameConfigForm;
