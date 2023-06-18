import React, { useState, useEffect } from "react";
import { socket } from "../../socket";
import { ConnectionState } from "../connection-state/ConnectionState";
import { ConnectionManager } from "../connection-manager/ConnectionManager";
import { Events } from "../events/Events";
import { MyForm } from "../my-form/MyForm";

export default function App() {
  const [isConnected, setIsConnected] = useState(socket.connected);
  const [fooEvents, setFooEvents] = useState([]);

  const handleButtonClick = () => {
    fetch("http://localhost:5000/callme", {
      method: "GET",
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
      <button onClick={handleButtonClick}>Fetch an api!</button>
    </div>
  );
}
