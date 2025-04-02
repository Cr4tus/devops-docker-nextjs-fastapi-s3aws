# DevOps Project: Next.js, FastAPI, and AWS S3 Integration

This project showcases a full-stack web application integrating a Next.js front-end with a FastAPI back-end, featuring AWS S3 integration (for scalable storage solutions). The application is containerized using Docker and orchestrated with Docker Compose, demonstrating a comprehensive DevOps workflow.

## Project Overview

- **Front-End**: Developed with [Next.js](https://nextjs.org/), a React-based framework that enables server-side rendering and static site generation for robust and performant user interfaces.

- **Back-End**: Built using [FastAPI](https://fastapi.tiangolo.com/), a modern, fast (high-performance), web framework for building APIs with Python 3.7+.

- **Storage Integration**: Incorporates [AWS S3](https://aws.amazon.com/s3/) for scalable and secure object storage, facilitating efficient handling of user-generated content and static assets.

- **Containerization**: Utilizes Docker to containerize both front-end and back-end services, ensuring consistency across development and production environments.

- **Orchestration**: Employs Docker Compose for defining and running multi-container Docker applications, streamlining the development and deployment processes.

## Repository Structure

- `nextjs-front-end/`: Contains the Next.js front-end application code.

- `python-fastapi-s3aws-api/`: Houses the FastAPI back-end application code.

- `docker-compose.yml`: Defines the Docker Compose configuration for orchestrating the multi-container application.

- `Makefile`: Provides convenient commands for building & managing the application lifecycle.

## Features

- **Responsive UI**: The Next.js front-end delivers a responsive and dynamic user interface, enhancing user experience across devices.

- **High-Performance API**: The FastAPI back-end ensures rapid responses and efficient handling of API requests.

- **Scalable Storage**: Integration with AWS S3 enables scalable storage solutions, accommodating growing data needs seamlessly.

- **Containerization**: Dockerization of services ensures environment consistency, simplifies deployment, and enhances scalability.

- **Orchestration**: Docker Compose facilitates the management of multi-container applications, streamlining development workflows.

- **CI/CD Pipeline**:  GitHub Actions automates the process of building and pushing Docker images to Docker Hub, ensuring a smooth deployment workflow.

    - [Back-end (public Docker Hub image)](https://hub.docker.com/repository/docker/cr4tus/devops-back-end/general)
    - [Front-end (public Docker Hub image)](https://hub.docker.com/repository/docker/cr4tus/devops-front-end/general)

## Getting Started

To set up and run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Cr4tus/devops-docker-nextjs-fastapi-s3aws.git
   cd devops-docker-nextjs-fastapi-s3aws
   ```

2. **Set Up Environment Variables**:
    
    Create a `.env` file within the `python-fastapi-s3aws-api/` folder & follow the template provided within `.env.example`

3. **Build and Start the Application**:
    ```bash
    docker-compose up
    ```
