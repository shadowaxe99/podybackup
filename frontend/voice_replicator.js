const WebRTC = require('webrtc');
const voiceReplicator = require('../backend/voice_replicator');

let localStream;
let peerConnection;

navigator.mediaDevices.getUserMedia({ audio: true })
  .then(stream => {
    localStream = stream;
  })
  .catch(error => {
    console.error('Error accessing media devices.', error);
  });

peerConnection = new WebRTC.RTCPeerConnection();

peerConnection.onicecandidate = function(event) {
  if (event.candidate) {
  } else {
  }
};

peerConnection.onaddstream = function(event) {
  const replicatedVoiceStream = voiceReplicator.replicateVoice(event.stream);
  const audioElement = document.getElementById('podcast-player');
  audioElement.srcObject = replicatedVoiceStream;
};

peerConnection.addStream(localStream);

peerConnection.createOffer()
  .then(offer => peerConnection.setLocalDescription(offer))
  .then(() => {
  })
  .catch(error => {
    console.error('Error creating offer.', error);
  });

peerConnection.onremotedescriptionset = function() {
  if (peerConnection.remoteDescription.type === 'offer') {
    peerConnection.createAnswer()
      .then(answer => peerConnection.setLocalDescription(answer))
      .then(() => {
      })
      .catch(error => {
        console.error('Error creating answer.', error);
      });
  }
};