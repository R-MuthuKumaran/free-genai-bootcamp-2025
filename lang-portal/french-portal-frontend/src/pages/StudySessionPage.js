import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import StudySessionShow from '../components/StudySessions/StudySessionShow';
import api from '../services/api';

function StudySessionPage() {
  const { id } = useParams();
  const [session, setSession] = useState(null);
  const [words, setWords] = useState([]);

  useEffect(() => {
    api.getStudySession(id).then(data => setSession(data));
    api.getStudySessionWords(id).then(data => setWords(data));
  }, [id]);

  return <StudySessionShow session={session} words={words} />;
}

export default StudySessionPage;