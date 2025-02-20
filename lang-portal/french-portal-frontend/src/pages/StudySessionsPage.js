import React, { useEffect, useState } from 'react';
import StudySessionsIndex from '../components/StudySessions/StudySessionsIndex';
import api from '../services/api';

function StudySessionsPage() {
  const [sessions, setSessions] = useState([]);

  useEffect(() => {
    api.getStudySessions().then(data => setSessions(data));
  }, []);

  return <StudySessionsIndex sessions={sessions} />;
}

export default StudySessionsPage;