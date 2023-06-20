export const createRoom = (gameconfigs) => {
  return fetch(`/room/create`, {
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ gameconfigs }),
  }).then((response) => response.json());
};
