# Poddy

Poddy is a web application that allows you to host your own podcast with anyone notable in the real world. It uses a voice replicator to simulate the voice of the guest, providing a fluid and realistic conversation experience.

## Features

- Real-time communication
- Voice replication
- Google Sign-In

## Code Structure and Architecture

The application is divided into two main parts: the frontend and the backend.

### Frontend

The frontend is built with HTML, CSS, and JavaScript. It uses Firebase for user authentication and WebRTC for real-time communication.

### Backend

The backend is built with Flask, a Python web framework. It uses SQLite for development and PostgreSQL for production. The backend also interacts with the OpenAI API to extract entities from the conversation and the Eleven Labs API to replicate voices.

## Dependencies

- Flask
- SQLite
- PostgreSQL
- OpenAI
- Eleven Labs
- Firebase
- WebRTC

## Deployment

The application is containerized using Docker and can be deployed on any platform that supports Docker. For orchestration, it includes a Kubernetes configuration.

## Getting Started

To run the application locally, you need to have Python and Docker installed on your machine. Then, you can clone the repository and run the application using the following commands:

```
git clone https://github.com/shadowaxe99/poddy.git
cd poddy
python3 backend/app.py
```

Then, open your web browser and navigate to `http://localhost:5000`.