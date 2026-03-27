# Django MariaDB Vector Demo

This repository demonstrates the integration of MariaDB's vector capabilities with Django using the `django-mariadb-vector` library. It showcases how to store vector embeddings, create vector indexes, and perform similarity searches within a Django application.

## Prerequisites

- **Docker & Docker Compose**: Used for containerized deployment of the application and the MariaDB database.
- **MariaDB 11.8.2+**: Required for native vector storage and similarity search functions.
- **Python 3.12+**: Required for running the application.
- **uv**: Modern Python package installer and resolver.

## Project Structure

- `src/articles`: The core application containing the `Article` model with vector fields.
- `src/config`: Django project settings and URL configuration.
- `docker-compose.yml`: Defines the backend and MariaDB services.
- `pyproject.toml`: Project dependencies and metadata.

## Getting Started

### 1. Environment Setup

Copy the example environment file and update it with your desired settings:

```bash
cp .env.example .env
```

Review the `.env` file and adjust database credentials, superuser passwords, and application ports as needed.

### 2. Run with Docker Compose

Build and start the services:

```bash
docker-compose up --build
```

The application will be accessible at `http://localhost:8001` (or the port specified in your `.env` file).

The `entrypoint.sh` script automatically:
- Runs database migrations.
- Creates a superuser (if `DJANGO_SUPERUSER_PASSWORD` is set in `.env`).
- Starts the Django development server.

### 3. Load Sample Data

Once the application is running, you can load sample articles with vector embeddings into the database:

```bash
docker-compose exec backend python src/manage.py loaddata 0001_article
```

### 4. Usage

- **Article List**: Navigate to `http://localhost:8001/` to see a list of articles.
- **Similar Articles**: Click on the "Similar Articles" link next to any article to see its most similar counterparts, calculated using MariaDB's vector similarity functions.

## Features Demonstrated

- **`MariaDBVectorField`**: Storing vector embeddings as a specialized field in Django models.
- **`MariaDBVectorIndex`**: Creating HNSW (Hierarchical Navigable Small World) indexes for efficient similarity search.
- **`RecommendationManager`**: Using a custom manager to perform `recommend()` queries based on vector similarity.

## Development

To run the project locally without Docker:

1.  **Install dependencies**:
    ```bash
    uv sync
    ```
2.  **Activate virtual environment**:
    ```bash
    .venv\Scripts\activate
    ```
3.  **Ensure MariaDB 11.8.2+ is running locally** and update your `.env` file to point to it.
4.  **Run migrations and start server**:
    ```bash
    python src/manage.py migrate
    python src/manage.py runserver
    ```


