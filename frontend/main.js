import firebase from 'firebase/app';
import 'firebase/auth';

const firebaseConfig = 'Your Firebase Configuration';

firebase.initializeApp(firebaseConfig);

document.getElementById('sign-up-form').addEventListener('submit', event => {
  event.preventDefault();
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  firebase.auth().createUserWithEmailAndPassword(email, password)
    .then((userCredential) => {
      // Signed in 
      var user = userCredential.user;
      console.log('User signed up:', user);
    })
    .catch((error) => {
      var errorCode = error.code;
      var errorMessage = error.message;
      console.error('Error signing up:', errorCode, errorMessage);
    });
});

document.getElementById('sign-in-form').addEventListener('submit', event => {
  event.preventDefault();
  const email = document.getElementById('sign-in-email').value;
  const password = document.getElementById('sign-in-password').value;
  firebase.auth().signInWithEmailAndPassword(email, password)
    .then((userCredential) => {
      // Signed in 
      var user = userCredential.user;
      console.log('User signed in:', user);
    })
    .catch((error) => {
      var errorCode = error.code;
      var errorMessage = error.message;
      console.error('Error signing in:', errorCode, errorMessage);
    });
});

firebase.auth().onAuthStateChanged((user) => {
  if (user) {
    // User is signed in
    console.log('User is signed in:', user);
    document.getElementById('welcome-message').textContent = `Welcome, ${user.email}!`;
    document.getElementById('sign-up-form').style.display = 'none';
    document.getElementById('sign-in-form').style.display = 'none';
    document.getElementById('sign-out').style.display = 'block';
  } else {
    // User is signed out
    console.log('User is signed out');
    document.getElementById('welcome-message').textContent = '';
    document.getElementById('sign-up-form').style.display = 'block';
    document.getElementById('sign-in-form').style.display = 'block';
    document.getElementById('sign-out').style.display = 'none';
  }
});

document.getElementById('sign-out').addEventListener('click', () => {
  firebase.auth().signOut().then(() => {
    // Sign-out successful.
    console.log('User signed out');
  }).catch((error) => {
    // An error happened.
    console.error('Error signing out:', error);
  });
});