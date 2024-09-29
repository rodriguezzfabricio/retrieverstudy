import React from 'react';
import './styles.css'; // Import your CSS file

const Home = () => {
  return (
    <div>
      <header>
        <div className="logo">
          <img src="retriever-logo.png" alt="Retriever Logo" />
          <h1>RETRIEVER STUDY</h1>
        </div>
        <div className="header-links">
          <a href="/home">Home</a>
          <a href="/login">Login</a>
        </div>
      </header>
      <section className="how-it-works">
        <h2>Find your study groups here!</h2>
        <h1>How it works:</h1>
        <div className="steps">
          <div className="step">
            <img src="person1.jpg" alt="Person 1" />
            <p>Choose your class! This is sorted by subject, so select your subject from the drop-down and select a class within.</p>
          </div>
          <div className="step">
            <img src="person2.jpg" alt="Person 2" />
            <p>Press "Join Study Team" and join the queue!</p>
          </div>
          <div className="step">
            <img src="person3.jpg" alt="Person 3" />
            <p>When you get into a group, you'll get an email to meet up with the date, time, and location!</p>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home;
