export const getHistory = () => {
  return fetch(`/room/load_history`, {
    method: "get",
  }).then((response) => response.json());
};

export const loadCheck = () => {
  return fetch(`/room/load_check`, {
    method: "get",
  }).then((response) => response.json());
};
