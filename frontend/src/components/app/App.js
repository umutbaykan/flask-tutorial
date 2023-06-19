import React, { useState, useEffect } from "react";
import { socket } from "../../socket";
import { ConnectionState } from "../connection-state/ConnectionState";
import { ConnectionManager } from "../connection-manager/ConnectionManager";
import { Events } from "../events/Events";
// import { MyForm } from "../my-form/MyForm";
import { InputForm } from "../input-form/InputForm";

export default function App() {
  const [isConnected, setIsConnected] = useState(socket.connected);
  const [fooEvents, setFooEvents] = useState([]);
  const [loginName, setLoginName] = useState("Roger");
  const [room, setRoom] = useState("")
  const [currentRoom, setCurrentRoom] = useState("")
  const [isLoggedIn, setIsLoggedIn] = useState(false)
  const [value, setValue] = useState("Initial message from frontend")

  const createRoom = () => {
    fetch("/createroom", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
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
    .then((data) => {
      console.log(data.room)
      setRoom(data.room)
    })
    .catch((error) => console.error(error));
  }

  const findMyRoomInSesssion = () => {
    fetch("/whereami", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include"
    })
    .then((response) => response.json())
    .then((data) => {
      if (data.room) {setCurrentRoom(data.room)}
      else {console.log(data.error)}
      })
    .catch((error) => console.error(error));
  }

  const login = () => {
    fetch("/auth/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include",
      body: JSON.stringify({"username": loginName, "password": "password"})
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
    .catch((error) => console.error(error));
    setIsLoggedIn(true)
  };

  const logout = () => {
    fetch("/auth/logout", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include"
    })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
    })
    .catch((error) => console.error(error));
    setRoom("")
    setIsLoggedIn(false)
  }

  const triggerFoo = (event) => {
    event.preventDefault();
    socket.emit("foo", value, () => {
      console.log("event emitted")
    });
  }

  const changeRoomTarget = (formInput) => {
    setRoom(formInput)
  }

  const changeValue = (formInput) => {
    setValue(formInput)
  }
  
  const joinRoom = (event) => {
    event.preventDefault()
    fetch("/joinroom", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({"room": room}),
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
    .then((data) => {
      setCurrentRoom(data.room)
    })
    .catch((error) => console.error(error));
  }

  useEffect(() => {
    findMyRoomInSesssion();
  }, [currentRoom])

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
    socket.on('foo', onFooEvent);

    return () => {
      socket.off("connect", onConnect);
      socket.off("disconnect", onDisconnect);
      socket.off('foo', onFooEvent);
    };
  }, []);

  return (
    <div className="App">
      {isLoggedIn ? (
      <>
      <h5>If you click connect below, your room will be</h5>
      <h3>{currentRoom}</h3>
      <ConnectionState isConnected={isConnected} />
      <Events events={fooEvents} />
      <ConnectionManager />
      <br>
      </br>
      <button onClick={triggerFoo}>Trigger foo</button>
      </>
      )
      :
      (<h5>Login to connect to a room</h5>)
    }
      <br>
      </br>
      <h3>Your current room target is</h3>
      <h1>{room}</h1>
      <h3>Login</h3>
      <input onChange={(e) => setLoginName(e.target.value)} />
      <button onClick={login}>Login</button>
      <button onClick={logout}>Logout</button>
      <button onClick={createRoom}>Create a random room number</button>
      {/* <MyForm /> */}
      <h3>Change message going to backend</h3>
      <InputForm callback={changeValue} buttonValue={"Change the message going to backend"}/>
      <h3>Change your room</h3>
      <InputForm callback={changeRoomTarget} buttonValue={"Change room target"}/>
      <button onClick={joinRoom}>Join the room you are targeting</button>

    </div>
  );
}
