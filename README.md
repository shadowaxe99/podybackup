# Poddy

Poddy is a podcast creation and streaming platform.

## Installation and Setup

1. Clone the repository:

```
git clone https://github.com/username/poddy.git
```

2. Navigate to the project directory:

```
cd poddy
```

3. Install the dependencies:

For the backend:

```
cd backend
pip install -r requirements.txt
```

For the frontend:

```
cd frontend
npm install
```

4. Configure the environment:

Create a `.env` file in the root directory and add the following environment variables:

```
DB_HOST=localhost
DB_USER=root
DB_PASS=password
DB_NAME=poddy
```

Replace `localhost`, `root`, `password`, and `poddy` with your actual database host, user, password, and name respectively.

5. Run the application:

For the backend:

```
flask run
```

For the frontend:

```
npm start
```

You should now be able to access the application at `http://localhost:3000`.

## Directory Structure

- `backend/`: Contains the backend code.
- `frontend/`: Contains the frontend code.
- `database/`: Contains the database scripts.
- `tests/`: Contains the test scripts.

## Configuration

The application uses the following environment variables:

- `DB_HOST`: The database host.
- `DB_USER`: The database user.
- `DB_PASS`: The database password.
- `DB_NAME`: The database name.

These can be set in a `.env` file in the root directory.

## Running the Application Locally

You can run the application locally for development by running `flask run` for the backend and `npm start` for the frontend.

## Testing

You can run the tests by running `pytest` for the backend and `npm test` for the frontend.

## CI/CD Process

The application uses GitHub Actions for the CI/CD process. The workflows are defined in the `.github/workflows` directory.

## Deployment

The application is deployed to a Kubernetes cluster. The Kubernetes configuration files are located in the `kubernetes/` directory.

## Contribution Guidelines

Please see the `CONTRIBUTING.md` file for the contribution guidelines.

## API Documentation

The API documentation is available at `http://localhost:5000/api/docs`.

## Troubleshooting

If you encounter any issues, please check the `TROUBLESHOOTING.md` file for common solutions.