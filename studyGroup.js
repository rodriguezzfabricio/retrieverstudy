import Student from './Student.js'; 

//StudyGroup Class
class StudyGroup {
    static maxSize = 8;
    #groupName;
    #courseName;
    #groupSize;
    #students;
    #meetTimes;
    #locations;

    // Constructor
    constructor(groupName, courseName){
        this.#groupName = groupName;
        this.#courseName = courseName;
        this.#students = [];
        this.#groupSize = 0;
    }

    // Setters
    setGroupName(newName){
        this.#groupName = newName;
    }

    setClass(newCourse){
        this.#courseName = newCourse;
    }

    // Getters
    getGroupName(){
        return this.#groupName;
    }

    getClass(){
        return this.#courseName;
    }

    // AddStudent
    addStudent(student){
        if (student instanceof Student){
            if (this.#groupSize < StudyGroup.maxSize) {  // Ensure group size does not exceed maxSize
                this.#students.push(student);
                this.#groupSize += 1;
                student.addStudyGroup(this);
                console.log(`${student.getName()} has been added to the group "${this.#groupName}".`);
            } else {
                console.log(`Cannot add ${student.getName()}. Group "${this.#groupName}" is full.`);
            }
        } else {
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
        console.log(`Course: ${this.#courseName}`);
        console.log(`Study Group: ${this.#groupName}`);
        console.log("Members:");
        this.#students.forEach(student => student.printDetails());
    }
}

export default StudyGroup
