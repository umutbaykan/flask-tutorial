import React, { useState, useEffect } from "react";
import { socket } from "../../socket";
import { ConnectionState } from "../connection-state/connectionState";
import { ConnectionManager } from "../connection-manager/connectionManager";
import { Events } from "../events/events";
import { MyForm } from "../my-form/myForm";

export default function App() {
  const [isConnected, setIsConnected] = useState(socket.connected);
  const [fooEvents, setFooEvents] = useState([]);

  const handleButtonClick = async () => {
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
    socket.on("foo", onFooEvent);

    return () => {
      socket.off("connect", onConnect);
      socket.off("disconnect", onDisconnect);
      socket.off("foo", onFooEvent);
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
