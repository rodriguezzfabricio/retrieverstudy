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
    addStudyGroup(Group){
        if (Group instanceof StudyGroup){
            if(!this.groupExists(Group.getGroupName())){
                this.#studyGroups.push(Group);
                console.log(`${Group.getGroupName()}, has been added to ${this.#courseName}.`);
            }
        }else{
            console.log(`Study group cannot be added`);
        }
    }

    // groupExists
    groupExists(groupName){
        return this.#studyGroups.some(group => group.getGroupName() === groupName);
    }
}