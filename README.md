Flask Hello World : Dockerized with CI/CD
Project Overview

This is a simple Flask application containerized using Docker and automated with GitHub Actions CI/CD.
The project demonstrates how to:

Build a Python Flask app

Containerize it with a multi-stage Dockerfile

Use Docker Compose for orchestration

Automate linting and build with GitHub Actions

 Project Structure
├── app.py
├── dockerfile
├── docker-compose.yml
├── requirements.txt
└── .github/
    └── workflows/
        └── ci.yml

 How It Works

app.py → Basic Flask route returning “Hello, World!”

dockerfile → Multi-stage Docker build for optimization

docker-compose.yml → Runs the app container easily

ci.yml → GitHub Actions pipeline for linting (flake8) + build verification

How to run Locally

Clone the repository:

git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>


How to build and run the container:

docker-compose up --build


Access the app:
Open http://localhost:5000
 in your browser.
You should see:

Hello, World! This Flask app is containerized.

 GitHub Actions CI/CD

Each push to the repository triggers an automatic pipeline that:

Installs dependencies

Runs flake8 to check code style

Builds the Docker image

Displays a  “Build succeeded” message on success
