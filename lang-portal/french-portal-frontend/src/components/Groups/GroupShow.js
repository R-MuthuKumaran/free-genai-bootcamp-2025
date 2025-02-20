import React from 'react';

function GroupShow({ group, words, sessions }) {
  if (!group || !words || !sessions) {
    return <div>Loading...</div>;
  }

  return (
    <div className="group-show">
      <h2>{group.name}</h2>
      <h3>Words</h3>
      <ul>
        {words.map(word => (
          <li key={word.id}>{word.word}</li>
        ))}
      </ul>
      <h3>Study Sessions</h3>
      <ul>
        {sessions.map(session => (
          <li key={session.id}>{session.date}</li>
        ))}
      </ul>
    </div>
  );
}

export default GroupShow;