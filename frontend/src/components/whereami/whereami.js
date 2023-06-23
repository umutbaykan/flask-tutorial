import React, {useState} from 'react';

const WhereAmI = () => {
    const [username, setUsername] = useState("")
    const [room, setRoom] = useState("")

    const handleUpdate = () => {
        fetch(`/whereami`, {
        method: "get",
        })
        .then((response) => response.json())
        .then((data) => {
            console.log(data)
            setRoom(data.room)
            setUsername(data.username)

        });
    }

    return (
        <>
        <h3>your ID: {username}</h3>
        <h3>your room in session: {room}</h3>
        <button onClick={handleUpdate}>Update</button>
        </>
    )

}

export default WhereAmI