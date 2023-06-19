import React, { useState } from "react";

export function RoomSpecifier() {
  const [value, setValue] = useState(null);

  const joinRoom = (event) => {
    event.preventDefault()
    fetch("/joinroom", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({"room": value}),
      credentials: "include"
    })
    .then((response) => {
      if (!response.ok) {
        response.json().then((errorData) => {
          console.error(errorData.error);
        });
      } else {
        return response.json();
      }
    })
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
  }

  return (
    <form onSubmit={joinRoom}>
      <input onChange={(e) => setValue(e.target.value)} />

      <button type="submit">
        Join a Room
      </button>
    </form>
  );
}
