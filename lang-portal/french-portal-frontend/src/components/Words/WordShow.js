import React from 'react';

function WordShow({ word }) {
  if (!word) {
    return <div>Loading...</div>;
  }

  return (
    <div className="word-show">
      <h2>{word.word}</h2>
      <p>Definition: {word.definition}</p>
      <p>Example: {word.example}</p>
    </div>
  );
}

export default WordShow;