// Import Firebase
import firebase from 'firebase/app';
import 'firebase/auth';

// Firebase configuration
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_AUTH_DOMAIN",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_STORAGE_BUCKET",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Function to sign up user
function signupUser(email, password) {
  return firebase.auth().createUserWithEmailAndPassword(email, password)
    .then((userCredential) => {
      // User signed up
      let user = userCredential.user;
      console.log('signupSuccess', user);
    })
    .catch((error) => {
      // Error occurred during sign up
      console.error(error);
    });
}

// Function to login user
function loginUser(email, password) {
  return firebase.auth().signInWithEmailAndPassword(email, password)
    .then((userCredential) => {
      // User logged in
      let user = userCredential.user;
      console.log('loginSuccess', user);
    })
    .catch((error) => {
      // Error occurred during login
      console.error(error);
    });
}

// Export functions
export { signupUser, loginUser };