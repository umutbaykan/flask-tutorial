export const auth = (username, password, route) => {
  return fetch(`/auth/${route}`, {
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ username, password }),
  }).then((response) => {
    if (response.ok) {
      return { success: true };
    } else {
      return response
        .json()
        .then((data) => ({ success: false, error: data.error }));
    }
  });
};

export const logout = () => {
  return fetch(`/auth/logout`, {
    method: "get",
  })
};