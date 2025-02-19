import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import DashboardPage from './pages/DashboardPage';
import StudyActivitiesPage from './pages/StudyActivitiesPage';
import StudyActivityPage from './pages/StudyActivityPage';
import WordsPage from './pages/WordsPage';
import WordPage from './pages/WordPage';
import GroupsPage from './pages/GroupsPage';
import GroupPage from './pages/GroupPage';
import SettingsPage from './pages/SettingsPage';
import './assets/styles/main.css';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/dashboard" component={DashboardPage} />
        <Route path="/study_activities/:id" component={StudyActivityPage} />
        <Route path="/study_activities" component={StudyActivitiesPage} />
        <Route path="/words/:id" component={WordPage} />
        <Route path="/words" component={WordsPage} />
        <Route path="/groups/:id" component={GroupPage} />
        <Route path="/groups" component={GroupsPage} />
        <Route path="/settings" component={SettingsPage} />
        <Route path="/" component={DashboardPage} />
      </Switch>
    </Router>
  );
}

export default App;