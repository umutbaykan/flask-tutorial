export const createRoom = (gameconfigs) => {
  return fetch(`/room/create`, {
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ gameconfigs }),
  }).then((response) => response.json())
  .then((data) => {
    if (data.error) {
      return { success: false, error: data.error }
    } else {
      return data
    }
  });
};