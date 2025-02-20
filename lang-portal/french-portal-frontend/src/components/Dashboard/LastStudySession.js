import React from 'react';

function LastStudySession({ data }) {
  if (!data) {
    return <div>Loading...</div>;
  }

  return (
    <div className="last-study-session">
      <h2>Last Study Session</h2>
      <p>Date: {data.date}</p>
      <p>Duration: {data.duration} minutes</p>
      <p>Correct Answers: {data.correctAnswers}</p>
      <p>Incorrect Answers: {data.incorrectAnswers}</p>
    </div>
  );
}

export default LastStudySession;