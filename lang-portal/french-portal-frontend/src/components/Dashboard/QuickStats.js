import React from 'react';

function QuickStats({ data }) {
  if (!data) {
    return <div>Loading...</div>;
  }

  return (
    <div className="quick-stats">
      <h2>Quick Stats</h2>
      <p>Total Study Time: {data.totalStudyTime} minutes</p>
      <p>Total Correct Answers: {data.totalCorrectAnswers}</p>
      <p>Total Incorrect Answers: {data.totalIncorrectAnswers}</p>
    </div>
  );
}

export default QuickStats;