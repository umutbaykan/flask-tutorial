import React, { useContext } from "react";

import { ChatContext } from "../../../../App";
import ChatForm from "../ChatForm/ChatForm";

const ChatBox = () => {
  const [chats] = useContext(ChatContext);

  return (
    <div className="container chat">
      {chats.map((chat, index) => (
        <p className="chat-message" key={index}>
          {chat}
        </p>
      ))}
      <ChatForm />
    </div>
  );
};

export default ChatBox;
