import React, { useEffect, useState } from 'react';
import GroupsIndex from '../components/Groups/GroupsIndex';
import api from '../services/api';

function GroupsPage() {
  const [groups, setGroups] = useState([]);

  useEffect(() => {
    api.getGroups().then(data => setGroups(data));
  }, []);

  return <GroupsIndex groups={groups} />;
}

export default GroupsPage;