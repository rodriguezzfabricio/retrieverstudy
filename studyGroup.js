import Student from './Student.js'; 

//StudyGroup Class

maxSize = 8;

class StudyGroup {
    #groupName;
    #Course;
    #groupSize;
    #students;
    #meetTime;
    #locations;

    // Constructor
    constructor(groupName, Course){
        this.#groupName = groupName;
        this.#Course = Course;
        this.#students = [];
    }

    // Setters
    setGroupName(newName){
        this.#groupName = newName;
    }

    setClass(newCourse){
        this.#Course = newCourse;
    }

    // Getters
    getGroupName(){
        return this.#groupName;
    }

    getClass(){
        return this.#Course;
    }

    // AddStudent
    addStudent(student){
        if (student instanceof Student){
            this.#students.push(student)
            console.log(`${student.getName()} has been added to the group "${this.#groupName}".`);
        }else{
            console.log("Invalid student. Please provide a valid Student object.");
        }
    }

    // RemoveStudent
    removeStudent(studentName) {
        const index = this.#students.findIndex(student => student.getName() === studentName);
        if (index !== -1) {
            console.log(`${this.#students[index].getName()} has been removed from the group "${this.#groupName}".`);
            this.#students.splice(index, 1);
        } else {
            console.log(`Student "${studentName}" not found in the group.`);
        }
    }

    // Method to print all students in the group
    printGroupDetails() {
        console.log(`Course: ${this.#Course}`);
        console.log(`Study Group: ${this.#groupName}`);
        console.log("Members:");
        this.#students.forEach(student => student.printDetails());
    }
}