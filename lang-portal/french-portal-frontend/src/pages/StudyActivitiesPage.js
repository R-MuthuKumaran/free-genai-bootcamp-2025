import React, { useEffect, useState } from 'react';
import StudyActivitiesIndex from '../components/StudyActivities/StudyActivitiesIndex';
import api from '../services/api';

function StudyActivitiesPage() {
  const [studyActivities, setStudyActivities] = useState([]);

  useEffect(() => {
    api.getStudyActivities().then(data => setStudyActivities(data));
  }, []);

  return <StudyActivitiesIndex activities={studyActivities} />;
}

export default StudyActivitiesPage;