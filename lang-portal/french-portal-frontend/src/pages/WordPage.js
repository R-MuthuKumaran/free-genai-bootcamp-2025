import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import WordShow from '../components/Words/WordShow';
import api from '../services/api';

function WordPage() {
  const { id } = useParams();
  const [word, setWord] = useState(null);

  useEffect(() => {
    api.getWord(id).then(data => setWord(data));
  }, [id]);

  return <WordShow word={word} />;
}

export default WordPage;