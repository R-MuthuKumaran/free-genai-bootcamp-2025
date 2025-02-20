import React from 'react';

function WordsIndex({ words }) {
  if (!words) {
    return <div>Loading...</div>;
  }

  return (
    <div className="words-index">
      <h2>Words</h2>
      <ul>
        {words.map(word => (
          <li key={word.id}>{word.word}</li>
        ))}
      </ul>
    </div>
  );
}

export default WordsIndex;