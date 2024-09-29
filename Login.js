// Login.js
import React from 'react';
import './styles.css'; // Assuming you moved the styles to a CSS file

const Login = () => {
  return (
    <div className="login-container">
      <h2>Login</h2>
      <form action="/login" method="POST">
        <input type="text" name="username" placeholder="Username" required />
        <input type="password" name="password" placeholder="Password" required />
        <input type="submit" value="Login" />
      </form>
      <p>
        Don't have an account? <a href="/signup">Sign up</a>
      </p>
    </div>
  );
};

export default Login;



