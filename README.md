# FastAPI + PostgreSQL CRUD Project

![FastAPI](https://img.shields.io/badge/FastAPI-CRUD-brightgreen) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue) ![React](https://img.shields.io/badge/Frontend-React-blue) ![Redis](https://img.shields.io/badge/Redis-Caching-red)

A CRUD (Create, Read, Update, Delete) application built with FastAPI, PostgreSQL, and React, with Redis integration for caching. The project demonstrates the basics of API development with FastAPI, relational database operations with PostgreSQL, frontend form integration using React, and caching responses using Redis.

## Features

- Backend API built with FastAPI to handle CRUD operations.
- Database integration using PostgreSQL.
- User registration form frontend built with React.
- Redis integration for caching API responses.
- Unit testing for backend functionality.

## Table of Contents

- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Frontend Setup](#frontend-setup)
- [Backend Setup](#backend-setup)
- [Running Tests](#running-tests)
- [Usage](#usage)
- [License](#license)

## Tech Stack

- **Backend**: FastAPI, PostgreSQL, Redis
- **Frontend**: React.js
- **Testing**: unittest

## Getting Started

Follow the steps below to set up both the frontend and backend of this project.

### Prerequisites

Ensure you have the following installed on your machine:

- Python 3.9+
- Node.js 14+
- Docker (for PostgreSQL and Redis setup)
- Git

## Frontend Setup

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Navigate to the `frontend` directory:

    ```bash
    cd frontend
    ```

3. Install dependencies:

    ```bash
    npm install
    ```

4. Start the React development server:

    ```bash
    npm start
    ```

    The React application should now be running at [http://localhost:3000](http://localhost:3000).

## Backend Setup

1. Navigate to the `backend` directory:

    ```bash
    cd backend
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Linux/macOS:

        ```bash
        source venv/bin/activate
        ```

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Set up PostgreSQL and Redis using Docker:

    ```bash
    docker-compose up -d
    ```

    This will set up PostgreSQL and Redis containers.

6. Create the PostgreSQL database:

    ```bash
    python create_db.py
    ```

7. Start the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

    The FastAPI server should now be running at [http://localhost:8000](http://localhost:8000).

## Running Tests

To run unit tests for the backend, use the following command:

```bash
pytest
