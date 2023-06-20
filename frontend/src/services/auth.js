const signUp = async (username, password) => {
  try {
    const response = await fetch('/auth/register', {
      method: 'post',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    });

    if (response.status === 201) {
      return { success: true };
    } else {
      return { error: 'Sign up failed' };
    }
  } catch (error) {
    return { error: 'An error occurred' };
  }
};

export default signUp;