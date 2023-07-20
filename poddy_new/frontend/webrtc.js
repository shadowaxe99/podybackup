// Importing required modules
import { authToken } from './auth.js';

// WebRTC configuration
const configuration = {
  iceServers: [
    {
      urls: 'stun:stun.l.google.com:19302'
    }
  ]
};

// Creating a new RTCPeerConnection
const peerConnection = new RTCPeerConnection(configuration);

// Function to start the podcast recording
function startRecording() {
  navigator.mediaDevices.getUserMedia({ audio: true, video: true })
    .then(stream => {
      stream.getTracks().forEach(track => peerConnection.addTrack(track, stream));
    })
    .catch(error => console.error('Error accessing media devices.', error));
}

// Function to stop the podcast recording
function stopRecording() {
  peerConnection.getSenders().forEach(sender => sender.track.stop());
}

// Function to handle offer creation and setting local description
function createOffer() {
  peerConnection.createOffer()
    .then(offer => peerConnection.setLocalDescription(offer))
    .then(() => {
      // Send the offer to the server
      const offer = peerConnection.localDescription;
      fetch('/webrtc-offer', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${authToken}`
        },
        body: JSON.stringify({ offer })
      });
    })
    .catch(error => console.error('Error creating offer.', error));
}

// Function to handle answer setting as remote description
function handleAnswer(answer) {
  const remoteDesc = new RTCSessionDescription(answer);
  peerConnection.setRemoteDescription(remoteDesc);
}

// Function to handle ICE candidate event
peerConnection.onicecandidate = event => {
  if (event.candidate) {
    // Send the ICE candidate to the server
    fetch('/webrtc-candidate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authToken}`
      },
      body: JSON.stringify({ candidate: event.candidate })
    });
  }
};

// Exporting functions
export { startRecording, stopRecording, createOffer, handleAnswer };