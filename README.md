# Django MariaDB Vector Demo

A minimal demo project showing how to build article recommendations using vector similarity in Django with MariaDB as the database.

The app stores articles, embeds their content into vectors, and then finds similar articles based on vector distance.

---

## Features

- Django application using MariaDB as the primary database
- Article model with text content
- Vector-based similarity search for recommendations
- Simple UI:
  - List of all articles
  - “Similar articles” view for a selected article
- Admin interface to add and manage articles


This repository demonstrates the integration of MariaDB's vector capabilities with Django using the `django-mariadb-vector` library. 
It showcases how to store vector embeddings, create vector indexes, and perform similarity searches within a Django application.

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

###  **Clone the repository**

   ```bash
   git clone https://github.com/lexxai/django-mariadb-vector-demo
   cd django-mariadb-vector-demo
   ```

### 1. Environment Setup

Copy the example environment file and update it with your desired settings:

```bash
cp .env.example .env
```

Review the `.env` file and adjust database credentials, superuser passwords, and application ports as needed.

### 2. Run with Docker Compose

#### Build and start the services:
```bash
docker compose up --build -d

up 5/5
 ✔ Image django-mariadb-vector-demo-backend       Built       2.5s
 ✔ Network django-mariadb-vector-demo_lan         Created     0.1s
 ✔ Volume django-mariadb-vector-demo_db_data      Created     0.0s
 ✔ Container django-mariadb-vector-demo-db-1      Healthy     21.3s
 ✔ Container django-mariadb-vector-demo-backend-1 Started     27.7s

```
#### Logs
```bash
docker compose logs -f backend

backend-1  | ** Starting Django make migrations
backend-1  | No changes detected
backend-1  | ** Starting Django migrate
backend-1  | Operations to perform:
backend-1  |   Apply all migrations: admin, articles, auth, contenttypes, sessions
backend-1  | Running migrations:
backend-1  |   Applying contenttypes.0001_initial... OK
backend-1  |   Applying auth.0001_initial... OK
backend-1  |   Applying admin.0001_initial... OK
backend-1  |   Applying admin.0002_logentry_remove_auto_add... OK
backend-1  |   Applying admin.0003_logentry_add_action_flag_choices... OK
backend-1  |   Applying articles.0001_initial... OK
backend-1  |   Applying contenttypes.0002_remove_content_type_name... OK
backend-1  |   Applying auth.0002_alter_permission_name_max_length... OK
backend-1  |   Applying auth.0003_alter_user_email_max_length... OK
backend-1  |   Applying auth.0004_alter_user_username_opts... OK
backend-1  |   Applying auth.0005_alter_user_last_login_null... OK
backend-1  |   Applying auth.0006_require_contenttypes_0002... OK
backend-1  |   Applying auth.0007_alter_validators_add_error_messages... OK
backend-1  |   Applying auth.0008_alter_user_username_max_length... OK
backend-1  |   Applying auth.0009_alter_user_last_name_max_length... OK
backend-1  |   Applying auth.0010_alter_group_name_max_length... OK
backend-1  |   Applying auth.0011_update_proxy_permissions... OK
backend-1  |   Applying auth.0012_alter_user_first_name_max_length... OK
backend-1  |   Applying sessions.0001_initial... OK
backend-1  | ** Starting Django create superuser
backend-1  | Superuser created successfully.
backend-1  | Starting Django...
backend-1  | Performing system checks...
backend-1  | 
backend-1  | System check identified no issues (0 silenced).
backend-1  | March 27, 2026 - 22:18:56
backend-1  | Django version 6.0.3, using settings 'config.settings'
backend-1  | Starting development server at http://0.0.0.0:8001/
backend-1  | Quit the server with CONTROL-C.
backend-1  | 
backend-1  | WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
backend-1  | For more information on production servers see: https://docs.djangoproject.com/en/6.0/howto/deployment/
```

The application will be accessible at `http://localhost:8001` (or the port specified in your `.env` file).

The `entrypoint.sh` script automatically:
- Runs database migrations.
- Creates a superuser (if `DJANGO_SUPERUSER_PASSWORD` is set in `.env`).
- Starts the Django development server.

### 3. Load Sample Data

Once the application is running, you can load sample articles with vector embeddings into the database:

```bash
docker compose exec backend python src/manage.py loaddata 0001_article

Installed 3 object(s) from 1 fixture(s)
```

### 4. Usage

- **Article List**: Navigate to `http://localhost:8001/articles/` to see a list of articles.
- **Similar Articles**: Click on the "Similar Articles" link next to any article to see its most similar counterparts, calculated using MariaDB's vector similarity functions.

## Features Demonstrated

- **`MariaDBVectorField`**: Storing vector embeddings as a specialized field in Django models.
- **`MariaDBVectorIndex`**: Creating HNSW (Hierarchical Navigable Small World) indexes for efficient similarity search.
- **`RecommendationManager`**: Using a custom manager to perform `recommend()` queries based on vector similarity.

## Administration

Navigate to `http://localhost:8001/admin/
- User is `admin`
- password is from your `.env` file.
- 

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

## Examples

- [README.md](docs/README.md)


## License

[MIT](https://choosealicense.com/licenses/mit/)