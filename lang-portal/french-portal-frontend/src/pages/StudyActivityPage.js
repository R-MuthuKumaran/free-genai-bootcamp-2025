import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import StudyActivityShow from '../components/StudyActivities/StudyActivityShow';
import api from '../services/api';

function StudyActivityPage() {
  const { id } = useParams();
  const [activity, setActivity] = useState(null);
  const [sessions, setSessions] = useState([]);

  useEffect(() => {
    api.getStudyActivity(id).then(data => setActivity(data));
    api.getStudyActivitySessions(id).then(data => setSessions(data));
  }, [id]);

  return <StudyActivityShow activity={activity} sessions={sessions} />;
}

export default StudyActivityPage;