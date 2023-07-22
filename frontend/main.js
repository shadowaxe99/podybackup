// Importing necessary modules
const auth = require('./auth.js');
const webrtc = require('./webrtc.js');

// DOM Elements
const loginButton = document.getElementById('loginButton');
const signupButton = document.getElementById('signupButton');
const podcastContainer = document.getElementById('podcastContainer');
const editPodcastButton = document.getElementById('editPodcastButton');
const publishPodcastButton = document.getElementById('publishPodcastButton');
const sharePodcastButton = document.getElementById('sharePodcastButton');
const searchPodcastInput = document.getElementById('searchPodcastInput');

// Variables
let userProfile = null;
let podcastList = [];
let currentPodcast = null;
let authToken = null;

// Event Listeners
loginButton.addEventListener('click', loginUser);
signupButton.addEventListener('click', signupUser);
editPodcastButton.addEventListener('click', editPodcast);
publishPodcastButton.addEventListener('click', publishPodcast);
sharePodcastButton.addEventListener('click', sharePodcast);
searchPodcastInput.addEventListener('keyup', searchPodcast);

// Functions
function loginUser() {
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  if (!validator.isAlphanumeric(username)) {
    alert('Username is not valid. Please enter only alphanumeric characters.');
    return;
  }

  if (!validator.isLength(password, { min: 6 })) {
    alert('Password is not valid. It should be at least 6 characters long.');
    return;
  }

  auth.login(username, password).then(token => {
    authToken = token;
    fetchUserProfile();
    fetchPodcasts();
  });
}

function signupUser() {
  auth.signup().then(token => {
    authToken = token;
    createUserProfile();
  });
}

function editPodcast() {
  if (currentPodcast) {
    openPodcastEditingInterface(currentPodcast);
  }
}

function publishPodcast() {
  if (!authToken) {
    alert('You must be logged in to publish a podcast.');
    return;
  }

  if (currentPodcast) {
    publishCurrentPodcast(currentPodcast);
  }
}

function sharePodcast() {
  if (currentPodcast) {
    shareCurrentPodcast(currentPodcast);
  }
}

function searchPodcast() {
  const query = searchPodcastInput.value;
  searchPodcastsBasedOnQuery(query);
}

// WebRTC setup
webrtc.setup().then(stream => {
  handleRealTimeCommunication(stream);
});