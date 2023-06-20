const signUp = (username, password) => {
  return fetch("/auth/register", {
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ username, password }),
  }).then((response) => {
    if (response.status === 201) {
      return { success: true };
    } else {
      return response
        .json()
        .then((data) => ({ success: false, error: data.error }));
    }
  });
};

export default signUp;
