export const auth = (username, password, route) => {
  return fetch(`/auth/${route}`, {
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ username, password }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.error) {
        return { success: false, error: data.error };
      } else {
        return {
          success: true,
          user_id: data.user_id,
          username: data.username,
        };
      }
    });
};

export const logout = () => {
  return fetch(`/auth/logout`, {
    method: "get",
  });
};
