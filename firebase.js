import firebase from "firebase";

const firebaseConfig = {
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  apiKey: "AIzaSyDO961JTHNCF5hIJJSRmY-NoVfery4D_qw",
  authDomain: "studyretrievers.firebaseapp.com",
  projectId: "studyretrievers",
  storageBucket: "studyretrievers.appspot.com",
  messagingSenderId: "1083348894148",
  appId: "1:1083348894148:web:5caba868e631a2c9612491",
  measurementId: "G-D11X3FRS8S"
};

const firebaseApp = firebase.initializeApp(firebaseConfig);

const db = firebaseApp.firestore();

export default db;
