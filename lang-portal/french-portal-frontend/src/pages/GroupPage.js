import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import GroupShow from '../components/Groups/GroupShow';
import api from '../services/api';

function GroupPage() {
  const { id } = useParams();
  const [group, setGroup] = useState(null);
  const [words, setWords] = useState([]);
  const [sessions, setSessions] = useState([]);

  useEffect(() => {
    api.getGroup(id).then(data => setGroup(data));
    api.getGroupWords(id).then(data => setWords(data));
    api.getGroupStudySessions(id).then(data => setSessions(data));
  }, [id]);

  return <GroupShow group={group} words={words} sessions={sessions} />;
}

export default GroupPage;