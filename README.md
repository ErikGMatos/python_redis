# Product Management API with Redis Caching and SQLite Storage

This project implements a Flask-based API for managing product information, utilizing Redis for caching and SQLite for persistent storage. It provides endpoints for creating and retrieving product data with efficient caching mechanisms.

The application is designed to demonstrate the integration of multiple data storage solutions and showcases best practices in structuring a Python web application. It leverages Redis for quick access to frequently requested data and SQLite for reliable, persistent storage of product information.

Key features include:
- RESTful API endpoints for product management
- Redis caching for improved read performance
- SQLite database for persistent storage
- Modular architecture with clear separation of concerns
- Comprehensive error handling and data validation

## Repository Structure

```
.
├── init
│   └── schema.sql
├── redis_raw.py
├── run.py
└── src
    ├── data
    │   ├── product_creator.py
    │   └── product_finder.py
    ├── http_types
    │   ├── http_request.py
    │   └── http_response.py
    ├── main
    │   ├── composer
    │   │   ├── product_creator_composer.py
    │   │   └── product_finder_composer.py
    │   ├── routes
    │   │   └── products_routes.py
    │   └── server
    │       └── server.py
    └── models
        ├── redis
        │   ├── respository
        │   │   ├── interfaces
        │   │   │   └── redis_repository.py
        │   │   └── redis_repository.py
        │   └── settings
        │       └── connection.py
        └── sqlite
            ├── repository
            │   ├── interfaces
            │   │   └── products_repository.py
            │   ├── products_repository_test.py
            │   └── products_repository.py
            └── settings
                └── connection.py
```

Key Files:
- `run.py`: Entry point for the application
- `src/main/server/server.py`: Flask application setup
- `src/main/routes/products_routes.py`: API route definitions
- `src/data/product_creator.py` and `src/data/product_finder.py`: Core business logic
- `src/models/redis/respository/redis_repository.py`: Redis interaction
- `src/models/sqlite/repository/products_repository.py`: SQLite interaction

## Usage Instructions

### Installation

Prerequisites:
- Python 3.7+
- Redis server
- SQLite

Steps:
1. Clone the repository
2. Install dependencies:
   ```
   pip3 install -r requirements.txt
   ```
3. Ensure Redis is running on localhost:6379
4. Initialize the SQLite database:
   ```
   sqlite3 storage.db < init/schema.sql
   ```

### Getting Started

To run the application:

```
python run.py
```

The server will start on `http://0.0.0.0:3000`.

### API Endpoints

1. Create a product:
   ```
   POST /products
   Content-Type: application/json

   {
     "name": "Example Product",
     "price": 19.99,
     "quantity": 100
   }
   ```

2. Retrieve a product:
   ```
   GET /products/{product_name}
   ```

### Configuration

- Redis connection: Modify `src/models/redis/settings/connection.py`
- SQLite connection: Modify `src/models/sqlite/settings/connection.py`

### Testing

Run the tests using pytest:

```
pytest src/models/sqlite/repository/products_repository_test.py
```

Note: Some tests are skipped due to database interactions.

### Troubleshooting

Common issues:

1. Redis connection error:
   - Error: `ConnectionError: Error 111 connecting to localhost:6379. Connection refused.`
   - Solution: Ensure Redis server is running on the specified host and port.

2. SQLite database not found:
   - Error: `sqlite3.OperationalError: no such table: products`
   - Solution: Run the SQLite initialization script as mentioned in the installation steps.

3. Import errors:
   - Error: `ModuleNotFoundError: No module named 'flask'`
   - Solution: Ensure all dependencies are installed using `pip install -r requirements.txt`

For debugging:
- Enable Flask debug mode in `run.py`
- Check application logs in the console output

## Data Flow

The application follows a request-response cycle for product management operations:

1. Client sends HTTP request to Flask server
2. Request is routed to appropriate handler in `products_routes.py`
3. Handler creates `HttpRequest` object and passes it to the relevant use case (Creator or Finder)
4. Use case interacts with Redis cache first:
   - For GET requests, checks cache for product data
   - For POST requests, updates cache after database operation
5. If cache miss or write operation, use case interacts with SQLite database
6. Response is formatted and returned to client

```
Client -> Flask Server -> Route Handler -> Use Case -> Redis Cache <-> SQLite Database
  ^                                                                        |
  |                                                                        |
  ------------------------------------------------------------------------
```

Note: The Redis cache has a 60-second TTL for product data to ensure eventual consistency with the SQLite database.