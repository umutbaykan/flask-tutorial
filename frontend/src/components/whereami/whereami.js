import React, {useState} from 'react';

const WhereAmI = () => {
    const [username, setUsername] = useState("")

    const handleUpdate = () => {
        fetch(`/whereami`, {
        method: "get",
        })
        .then((response) => response.json())
        .then((data) => {
            console.log(data)
            setUsername(data.username)

        });
    }

    return (
        <>
        <h3>your ID: {username}</h3>
        <button onClick={handleUpdate}>Update</button>
        </>
    )

}

export default WhereAmI