import React, { useContext } from "react";
import { ChatContext } from "../../../../App";

const ChatBox = () => {
    const chats = useContext(ChatContext);

    return (
    <p>{chats.user} has joined {chats.room}</p>
    )
  ;
}

export default ChatBox

