import React, { useEffect, useState } from 'react';
import Dashboard from '../components/Dashboard/Dashboard';
import api from '../services/api';

function DashboardPage() {
  const [lastStudySession, setLastStudySession] = useState(null);
  const [studyProgress, setStudyProgress] = useState(null);
  const [quickStats, setQuickStats] = useState(null);

  useEffect(() => {
    api.getLastStudySession().then(data => setLastStudySession(data));
    api.getStudyProgress().then(data => setStudyProgress(data));
    api.getQuickStats().then(data => setQuickStats(data));
  }, []);

  return (
    <Dashboard
      lastStudySession={lastStudySession}
      studyProgress={studyProgress}
      quickStats={quickStats}
    />
  );
}

export default DashboardPage;