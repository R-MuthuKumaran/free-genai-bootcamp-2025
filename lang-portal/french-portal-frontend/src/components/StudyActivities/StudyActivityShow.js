import React from 'react';

function StudyActivityShow({ activity, sessions }) {
  if (!activity || !sessions) {
    return <div>Loading...</div>;
  }

  return (
    <div className="study-activity-show">
      <h2>{activity.name}</h2>
      <h3>Study Sessions</h3>
      <ul>
        {sessions.map(session => (
          <li key={session.id}>{session.date}</li>
        ))}
      </ul>
    </div>
  );
}

export default StudyActivityShow;