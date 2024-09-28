// Student Class
class Student {
    #name = "";
    #year = 0;
    #major = "";
    #id = "";
    #phoneNumber;
    #email;


    // Constructor
    constructor(name, year, major, id) {
        this.#name = name;
        this.#year = year;
        this.#major = major;
        this.#id = id;
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

    printDetails() {
        console.log(`Name: ${this.#name}, Year: ${this.#year}, Major: ${this.#major}, ID: ${this.#id}, `);
    }

}