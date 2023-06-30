export const getHistory = () => {
    return fetch(`/room/load_history`, {
      method: "get",
    })
      .then((response) => response.json())
  };
  