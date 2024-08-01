```markdown
# DICOM Handling Django Application

## Overview

This project is a Django application for handling DICOM files, which includes an endpoint for uploading DICOM files and extracting basic information from them.
The application is containerized using Docker.

## Prerequisites

Make sure you have the following installed on your system:

- Docker
- Docker Compose

## Building and Running the Application

Follow these steps to build and run the application using Docker:

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/itsnegaar/dicom-handling-app.git
cd dicom-handling-app
```

### 2. Build the Docker Image

Build the Docker image using Docker Compose:

```bash
docker-compose build
```

This command will read the instructions from your `Dockerfile` and create a Docker image named `dicom-handling-app_web`.

### 3. Run the Application

Run the application using Docker Compose:

```bash
docker-compose up
```

This command will start the services defined in your `docker-compose.yml` file. The Django development server will start, and you can access the application at `http://localhost:8000`.

### 4. Stopping the Application

To stop the application, press `Ctrl+C` in the terminal where `docker-compose up` is running, or run:

```bash
docker-compose down
```

This command will stop and remove the containers defined in the `docker-compose.yml` file.

### 5. Accessing the Application

After running `docker-compose up`, you can access the Django application at `http://localhost:8000`.

## Dockerfile

This is the Dockerfile used to build the Docker image:

```dockerfile
FROM python:3.11-slim

LABEL authors="negar"

# Set environment variable
ENV PYTHONUNBUFFERED 1

# Upgrade pip
RUN pip3 install --upgrade pip

# Create and set the working directory
RUN mkdir /app
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip3 --timeout=5000 install --no-cache-dir -r ./requirements.txt

# Copy the project files into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## Docker Compose File

This is the docker-compose.yml file used to manage multi-container Docker applications:

```yaml
version: '3.8'

services:
  web:
    build: .
    command: >
      sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
    volumes:
      - .:/app
    ports:
      - "8000:8000"
```

## Notes

- Ensure that the `requirements.txt` file is in the root of your project directory.
- The application will automatically apply any database migrations when it starts up.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

This README.md file contains all the necessary information to set up, build, and run your Dockerized Django application. It includes instructions, Dockerfile content, and the docker-compose.yml content for clarity and ease of use.