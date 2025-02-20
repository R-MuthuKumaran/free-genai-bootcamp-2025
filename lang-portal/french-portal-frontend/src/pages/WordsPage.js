import React, { useEffect, useState } from 'react';
import WordsIndex from '../components/Words/WordsIndex';
import api from '../services/api';

function WordsPage() {
  const [words, setWords] = useState([]);

  useEffect(() => {
    api.getWords().then(data => setWords(data));
  }, []);

  return <WordsIndex words={words} />;
}

export default WordsPage;