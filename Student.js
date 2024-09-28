import StudyGroup from './studyGroup.js'; 

// Student Class
class Student {
    #name = "";
    #year = 0;
    #major = "";
    #id = "";
    #phoneNumber;
    #email = "";
    #studyGroups;
    #password = "";


    // Constructor
    constructor(name, year, major, id, password, email) {
        this.#name = name;
        this.#year = year;
        this.#major = major;
        this.#id = id;
        this.#password = password;
        this.#email = email;
    }

    // Setters
    setName(name){
        this.#name = name;
    }

    setYear(year){
        this.#year = year;
    }

    setMajor(major){
        this.#major = major;
    }

    setID(id){
        this.#id = id;
    }

    setphoneNumber(number){
        this.#phoneNumber = number;
    }

    setEmail(email){
        this.#email = email;
    }
    
    setPassword(password){
        this.#password = password;
    }

    // Getters
    getName(){
        return this.#name;
    }

    getYear(){
        return this.#name;
    }

    getMajor(){
        return this.#major;
    }

    getID(){
        return this.#id;
    }

    getPhoneNumber(){
        return this.#phoneNumber;
    }

    getPassword(){
        return this.#password;
    }

    getEmail(){
        return this.#email;
    }

    // addStudyGroup

    addStudyGroup(Group){
        if (Group instanceof StudyGroup){
            if (!this.groupExists(Group.getGroupName)){
                this.#studyGroups.push(Group);
            }else{

            }
        }
    }

    groupExists(groupName){
        return this.#studyGroups.some(group => group.getGroupName() === groupName);
    }

    // Print Deatils
    printDetails() { 
        console.log(`Name: ${this.#name}, Year: ${this.#year}, Major: ${this.#major}, ID: ${this.#id}, `);
        console.log()
    }
}   

export default Student;
