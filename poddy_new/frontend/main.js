// Importing necessary modules
import * as auth from './auth.js';
import * as webrtc from './webrtc.js';

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
  auth.login().then(token => {
    authToken = token;
    // Fetch user profile and podcasts
    fetchUserProfile();
    fetchPodcasts();
  });
}

function signupUser() {
  auth.signup().then(token => {
    authToken = token;
    // Create new user profile
    createUserProfile();
  });
}

function editPodcast() {
  if (currentPodcast) {
    // Open podcast editing interface
    openPodcastEditor();
  }
}

function publishPodcast() {
  if (currentPodcast) {
    // Publish current podcast
    publishCurrentPodcast();
  }
}

function sharePodcast() {
  if (currentPodcast) {
    // Share current podcast
    shareCurrentPodcast();
  }
}

function searchPodcast() {
  const query = searchPodcastInput.value;
  // Search podcasts based on query
  searchPodcasts(query);
}

// WebRTC setup
webrtc.setup().then(stream => {
  // Handle real-time communication
  handleRealTimeCommunication(stream);
});