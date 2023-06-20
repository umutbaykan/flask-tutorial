export const createRoom = (gameconfigs) => {
  return fetch(`/room/create`, {
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ gameconfigs }),
  }).then((response) => {
    if (!response.ok) {
      return { success: false, error: "Server is down, please try again later." };
    } else {
      return response
        .json()
        .then((data) => ({ success: true, room: data.room }));
    }
  });
} 

