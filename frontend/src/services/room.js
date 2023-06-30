export const createRoom = (gameconfigs) => {
  return fetch(`/room/create`, {
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(gameconfigs),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.error) {
        return { success: false, error: data.error };
      } else {
        return data;
      }
    });
};

export const joinRoom = (game_id) => {
  return fetch(`/room/join`, {
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ room: game_id }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.error) {
        return { success: false, error: data.error };
      } else {
        return { success: true };
      }
    });
};

export const loadRoom = (game_id) => {
  return fetch(`/room/load`, {
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ room: game_id }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.error) {
        return { success: false, error: data.error };
      } else {
        return { success: true };
      }
    });
};

