# BittensorDividends
An asynchronous API service for querying Bittensor blockchain data and performing sentiment-based staking operations.


## Project Structure

```
src/
├── api/                  # API endpoints
├── core/                 # Authentication and security & App Config  & App Lifecycle Events
├── db/                   # Database models
├── services/             # Third Party Services
├── tests/                # API Unit Tests
├── celery_worker.py      # Celery background tasks

main.py                   # FastAPI application

docker-compose.yml        # Docker Compose configuration
Dockerfile                # Docker image specification
requirements.txt          # Python dependencies
```