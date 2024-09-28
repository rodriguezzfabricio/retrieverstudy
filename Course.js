import StudyGroup from './studyGroup.js'; 

// Course
class Course {
    #courseName;
    #studyGroups;
    #studyGroupSize = 0;
    #students = 0;

    constructor(courseName, studentCount){
        this.#courseName = courseName;
        this.#studyGroups = [];
        this.#studyGroupSize = 0;
        this.#students = studentCount;
    }

    // Setters 
    setCourseName(newCourseName){
        this.#courseName = newCourseName;
    }

    // Getters
    getCourseName(){
        return this.#courseName;
    }

    // addStudyGroup
    addStudyGroup(groupName){
        //let groupName = prompt("Enter Group Name: ");
        if(!this.groupExists(groupName)){
            let Group = new StudyGroup(groupName, this.#courseName);
            this.#studyGroups.push(Group);
            this.#studyGroupSize += 1;
            console.log(`${groupName}, has been added to ${this.#courseName}.`);
        }else{
            console.log(`Study group cannot be added`);
        }
    }

    // groupExists
    groupExists(groupName){
        return this.#studyGroups.some(group => group.getGroupName() === groupName);
    }

    // removeGroup
    removeGroup(groupName){
        const index = this.#studyGroups.findIndex(group => group.getName() === groupName);
        if (index !== -1) {
            console.log(`${this.#studyGroups[index].getName()} has been removed from the Course "${this.#courseName}".`);
            this.#studyGroups.splice(index, 1);
        } else {
            console.log(`Group "${groupName}" not found in the group.`);
        }
    }
}

export default Course;
