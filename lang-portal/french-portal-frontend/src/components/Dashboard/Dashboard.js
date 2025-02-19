import React from 'react';
import LastStudySession from './LastStudySession';
import StudyProgress from './StudyProgress';
import QuickStats from './QuickStats';
import StartStudyingButton from './StartStudyingButton';

function Dashboard({ lastStudySession, studyProgress, quickStats }) {
  return (
    <div className="dashboard">
      <LastStudySession data={lastStudySession} />
      <StudyProgress data={studyProgress} />
      <QuickStats data={quickStats} />
      <StartStudyingButton />
    </div>
  );
}

export default Dashboard;