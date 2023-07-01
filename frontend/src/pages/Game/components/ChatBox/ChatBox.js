import React, { useContext } from "react";

import { ChatContext } from "../../../../App";
import ChatForm from "../ChatForm/ChatForm";

const ChatBox = () => {
  const [chats] = useContext(ChatContext);

  return (
    <div className="container chat">
      <div className="container message">
        {chats.map((chat, index) => (
          <p className="chat-message" key={index}>
            {chat}
          </p>
        ))}
      </div>
      <ChatForm />
    </div>
  );
};

export default ChatBox;
