const API_BASE_URL = 'http://localhost:8000/api';

const api = {
  getLastStudySession: async () => {
    const response = await fetch(`${API_BASE_URL}/dashboard/last_study_session`);
    return response.json();
  },
  getStudyProgress: async () => {
    const response = await fetch(`${API_BASE_URL}/dashboard/study_progress`);
    return response.json();
  },
  getQuickStats: async () => {
    const response = await fetch(`${API_BASE_URL}/dashboard/quick_stats`);
    return response.json();
  },
  getStudyActivities: async () => {
    const response = await fetch(`${API_BASE_URL}/study_activities`);
    return response.json();
  },
  getStudyActivity: async (id) => {
    const response = await fetch(`${API_BASE_URL}/study_activities/${id}`);
    return response.json();
  },
  getStudyActivitySessions: async (id) => {
    const response = await fetch(`${API_BASE_URL}/study_activities/${id}/study_sessions`);
    return response.json();
  },
  launchStudyActivity: async (data) => {
    const response = await fetch(`${API_BASE_URL}/study_activities`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
    return response.json();
  },
  getWords: async () => {
    const response = await fetch(`${API_BASE_URL}/words`);
    return response.json();
  },
  getWord: async (id) => {
    const response = await fetch(`${API_BASE_URL}/words/${id}`);
    return response.json();
  },
  getGroups: async () => {
    const response = await fetch(`${API_BASE_URL}/groups`);
    return response.json();
  },
  getGroup: async (id) => {
    const response = await fetch(`${API_BASE_URL}/groups/${id}`);
    return response.json();
  },
  getGroupWords: async (id) => {
    const response = await fetch(`${API_BASE_URL}/groups/${id}/words`);
    return response.json();
  },
  getGroupStudySessions: async (id) => {
    const response = await fetch(`${API_BASE_URL}/groups/${id}/study_sessions`);
    return response.json();
  },
  getStudySessions: async () => {
    const response = await fetch(`${API_BASE_URL}/study_sessions`);
    return response.json();
  },
  getStudySession: async (id) => {
    const response = await fetch(`${API_BASE_URL}/study_sessions/${id}`);
    return response.json();
  },
  getStudySessionWords: async (id) => {
    const response = await fetch(`${API_BASE_URL}/study_sessions/${id}/words`);
    return response.json();
  },
  resetHistory: async () => {
    const response = await fetch(`${API_BASE_URL}/reset_history`, {
      method: 'POST',
    });
    return response.json();
  },
  fullReset: async () => {
    const response = await fetch(`${API_BASE_URL}/full_reset`, {
      method: 'POST',
    });
    return response.json();
  },
};

export default api;