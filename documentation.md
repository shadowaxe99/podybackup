# Poddy Documentation

## Code Architecture

The application is divided into two main parts: the backend and the frontend.

The backend is a Flask application that handles user authentication, podcast management, voice replication, and real-time communication. It uses SQLite for development and PostgreSQL for production. The backend also interacts with Firebase Auth for user authentication, OpenAI API for language processing, Eleven Labs API for voice replication, and WebRTC for real-time communication.

The frontend is a simple HTML/CSS/JavaScript application that interacts with the backend. It uses Firebase Auth for user authentication and WebRTC for real-time communication.

## Requirements

- Python 3.8 or higher
- Node.js 14 or higher
- Firebase account
- OpenAI account
- Eleven Labs account

## Deployment

The application can be deployed using Docker and Kubernetes. A Dockerfile is provided for building a Docker image of the application, and a Kubernetes configuration file is provided for deploying the application to a Kubernetes cluster.

To build the Docker image, run the following command:

```
docker build -t poddy:latest .
```

To deploy the application to a Kubernetes cluster, run the following command:

```
kubectl apply -f kubernetes_config.yaml
```

## Contributing

If you want to contribute to this project, please feel free to submit a pull request or open an issue on GitHub.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.