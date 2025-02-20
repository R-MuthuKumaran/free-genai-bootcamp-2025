import React from 'react';
import { useHistory } from 'react-router-dom';

function StartStudyingButton() {
  const history = useHistory();

  const handleClick = () => {
    history.push('/study_activities');
  };

  return (
    <button onClick={handleClick} className="start-studying-button">
      Start Studying
    </button>
  );
}

export default StartStudyingButton;