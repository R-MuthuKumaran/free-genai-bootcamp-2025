import React from 'react';

function GroupsIndex({ groups }) {
  if (!groups) {
    return <div>Loading...</div>;
  }

  return (
    <div className="groups-index">
      <h2>Groups</h2>
      <ul>
        {groups.map(group => (
          <li key={group.id}>{group.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default GroupsIndex;