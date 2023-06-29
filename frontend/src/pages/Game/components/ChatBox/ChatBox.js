import "./ChatBox.css";
import React, { useContext } from "react";

import { ChatContext } from "../../../../App";
import ChatForm from "../ChatForm/ChatForm";

const ChatBox = () => {
  const [chats] = useContext(ChatContext);

  return (
    <div className="chat-container">
      {chats.map((chat, index) => (
        <ul className="chat-message" key={index}>
          {chat}
        </ul>
      ))}
      <ChatForm />
    </div>
  );
};

export default ChatBox;
