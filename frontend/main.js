```javascript
// Importing necessary modules
import { VoiceReplicator } from './voice_replicator.js';

// Initializing WebRTC
let peerConnection;
const configuration = {'iceServers': [{'urls': 'stun:stun.l.google.com:19302'}]};
peerConnection = new RTCPeerConnection(configuration);

// DOM Elements
const startButton = document.getElementById('start-call');
const podcastPlayer = document.getElementById('podcast-player');
const guestList = document.getElementById('guest-list');

// Voice Replicator
let voiceReplicator = new VoiceReplicator();

// Event Listeners
startButton.addEventListener('click', startCall);

// Function to start the call
function startCall() {
    navigator.mediaDevices.getUserMedia({audio: true, video: false})
    .then(stream => {
        stream.getTracks().forEach(track => peerConnection.addTrack(track, stream));
    })
    .catch(error => console.log(error));

    peerConnection.createOffer()
    .then(offer => peerConnection.setLocalDescription(offer))
    .then(() => {
        // Send the offer to the remote peer using the signaling server
    });

    peerConnection.ontrack = function(event) {
        // Get the stream from the event and add it to the podcast player
        podcastPlayer.srcObject = event.streams[0];
    };
}

// Function to update the guest list
function updateGuestList(users) {
    guestList.innerHTML = '';
    users.forEach(user => {
        let listItem = document.createElement('li');
        listItem.textContent = `${user.name}, ${user.age}`;
        guestList.appendChild(listItem);
    });
}

// Function to replicate guest voice
function replicateGuestVoice(user) {
    voiceReplicator.replicate(user.name)
    .then(voiceData => {
        // Use the voice data
    });
}
```