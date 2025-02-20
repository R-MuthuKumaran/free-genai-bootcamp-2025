import React from 'react';

function StudyActivitiesIndex({ activities }) {
  if (!activities) {
    return <div>Loading...</div>;
  }

  return (
    <div className="study-activities-index">
      <h2>Study Activities</h2>
      <ul>
        {activities.map(activity => (
          <li key={activity.id}>{activity.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default StudyActivitiesIndex;