import React, { useContext } from "react";

import { ChatContext } from "../../../../App";

const ChatBox = () => {
    const [chats, ] = useContext(ChatContext);

    return (
    <div>
    <h5>Here is the chat</h5>
    {chats.map((chat, index) => (
    <li key={index}>{chat}</li>
    ))}
    </div>
    )
  ;
}

export default ChatBox

