import React, { useState, useEffect } from 'react';
import axios from 'axios';
import MessageList from './components/MessageList';
import AnnouncementList from './components/AnnouncementList';
import TaskList from './components/TaskList';
import Gradebook from './components/Gradebook';
import FileUpload from './components/FileUpload';

function App() {
    const [messages, setMessages] = useState([]);
    const [announcements, setAnnouncements] = useState([]);
    const [tasks, setTasks] = useState([]);
    const [grades, setGrades] = useState([]);
    const [files, setFiles] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const [messageResponse, announcementResponse, taskResponse, gradeResponse, fileResponse] = await Promise.all([
                axios.get('/api/messages/'),
                axios.get('/api/announcements/'),
                axios.get('/api/tasks/'),
                axios.get('/api/grades/'),
                axios.get('/api/files/')
            ]);

            setMessages(messageResponse.data);
            setAnnouncements(announcementResponse.data);
            setTasks(taskResponse.data);
            setGrades(gradeResponse.data);
            setFiles(fileResponse.data);
        };
        fetchData();
    }, []);

    // ... rest of the component logic for rendering messages, announcements, tasks, grades, and files

    return (
        <div>
            <MessageList messages={messages} />
            <AnnouncementList announcements={announcements} />
            <TaskList tasks={tasks} />
            <Gradebook grades={grades} />
            <FileUpload files={files} />
        </div>
    );
}

export default App;