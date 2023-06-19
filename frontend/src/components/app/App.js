import React, { useState, useEffect } from "react";
import { socket } from "../../socket";
import { ConnectionState } from "../connection-state/ConnectionState";
import { ConnectionManager } from "../connection-manager/ConnectionManager";
import { Events } from "../events/Events";
import { MyForm } from "../my-form/MyForm";

export default function App() {
  const [isConnected, setIsConnected] = useState(socket.connected);
  const [fooEvents, setFooEvents] = useState([]);
  const [room, setRoom] = useState('room1')

  const handleButtonClick = () => {
    fetch("/join", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include",
      body: JSON.stringify({"room": room})
    })
      .then((response) => response.json())
      .then((data) => console.log(data));
  };

  const checkRoom = () => {
    fetch("/someroom", {
      method: "GET",
      credentials: "include",
    })
      .then((response) => response.json())
      .then((data) => console.log(data));
  };

  const login = () => {
    fetch("/auth/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include",
      body: JSON.stringify({"username": "dRogira", "password": "password"})
    })
      .then((response) => response.json())
      .then((data) => console.log(data));
  };

  useEffect(() => {
    function onConnect() {
      setIsConnected(true);
    }

    function onDisconnect() {
      setIsConnected(false);
    }

    function onFooEvent(value) {
      setFooEvents((previous) => [...previous, value]);
    }

    socket.on("connect", onConnect);
    socket.on("disconnect", onDisconnect);
    socket.on("respond-something", onFooEvent);

    return () => {
      socket.off("connect", onConnect);
      socket.off("disconnect", onDisconnect);
      socket.off("respond-something", onFooEvent);
    };
  }, []);

  return (
    <div className="App">
      <ConnectionState isConnected={isConnected} />
      <Events events={fooEvents} />
      <ConnectionManager />
      <MyForm />
      <button onClick={handleButtonClick}>Join a room</button>
      <button onClick={checkRoom}>check room</button>
      <br></br>
      <button onClick={() => setRoom("room2")}>change to room 2</button>
      <button onClick={() => setRoom("room1")}>change to room 1</button>
      <button onClick={login}>login first</button>
    </div>
  );
}
