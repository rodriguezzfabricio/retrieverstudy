import React, { useState } from 'react';
import Student from './components/Student';
import Course from './components/Course';
import StudyGroup from './components/StudyGroup';

const App = () => {
    // State to store course information
    const [courses, setCourses] = useState([]);
    const [students, setStudents] = useState([]);

    // Example: Create new instances of classes and update state
    const addStudent = () => {
        const newStudent = new Student('Alice', 2, 'Computer Science', '001');
        setStudents([...students, newStudent]);
    };

    return (
        <div>
            <h1>Study Group Finder</h1>
            <button onClick={addStudent}>Add Student</button>
            {students.map((student, index) => (
                <div key={index}>
                    {student.getName()} - {student.getMajor()}
                </div>
            ))}
        </div>
    );
};

export default App;


