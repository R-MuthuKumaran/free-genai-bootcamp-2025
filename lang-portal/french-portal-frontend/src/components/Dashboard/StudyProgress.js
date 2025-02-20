import React from 'react';

function StudyProgress({ data }) {
  if (!data) {
    return <div>Loading...</div>;
  }

  return (
    <div className="study-progress">
      <h2>Study Progress</h2>
      <p>Completed Lessons: {data.completedLessons}</p>
      <p>Current Streak: {data.currentStreak} days</p>
      <p>Longest Streak: {data.longestStreak} days</p>
    </div>
  );
}

export default StudyProgress;