import React from 'react';
import api from '../../services/api';

function Settings() {
  const handleResetHistory = async () => {
    await api.resetHistory();
    alert('History reset successfully');
  };

  const handleFullReset = async () => {
    await api.fullReset();
    alert('Full reset successfully');
  };

  return (
    <div className="settings">
      <h2>Settings</h2>
      <button onClick={handleResetHistory}>Reset History</button>
      <button onClick={handleFullReset}>Full Reset</button>
    </div>
  );
}

export default Settings;