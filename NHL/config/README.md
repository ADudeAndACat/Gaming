# Configuration Directory

This directory contains configuration files for different environments and components.

## Purpose
- Store environment-specific settings
- Configure application behavior
- Manage logging settings
- Define API endpoints and credentials
- Set database connection parameters

## Configuration Files (to be created)

### development.yaml
Development environment configuration:
```yaml
database:
  url: sqlite:///data/nhl_dev.db
  echo: true  # Log SQL queries

api:
  base_url: https://api-web.nhle.com/v1
  timeout: 30
  rate_limit: 100  # requests per minute
  cache_enabled: true
  cache_ttl: 3600

logging:
  level: DEBUG
  format: detailed
  file: logs/nhl_dev.log

features:
  enable_ml_predictions: false
  enable_real_time_updates: false
```

### production.yaml
Production environment configuration:
```yaml
database:
  url: postgresql://user:pass@localhost:5432/nhl_prod
  pool_size: 20
  echo: false

api:
  base_url: https://api-web.nhle.com/v1
  timeout: 10
  rate_limit: 50
  cache_enabled: true
  cache_ttl: 1800

logging:
  level: INFO
  format: json
  file: /var/log/nhl/app.log

features:
  enable_ml_predictions: true
  enable_real_time_updates: true
```

### logging.yaml
Logging configuration:
```yaml
version: 1
disable_existing_loggers: false

formatters:
  simple:
    format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
  detailed:
    format: '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
  json:
    class: pythonjsonlogger.jsonlogger.JsonFormatter

handlers:
  console:
    class: logging.StreamHandler
    formatter: simple
    stream: ext://sys.stdout
  
  file:
    class: logging.handlers.RotatingFileHandler
    formatter: detailed
    filename: logs/nhl.log
    maxBytes: 10485760  # 10MB
    backupCount: 5

loggers:
  src:
    level: DEBUG
    handlers: [console, file]
    propagate: false

root:
  level: INFO
  handlers: [console]
```

## Environment Variables

Create a `.env` file in the project root (not in this directory):
```bash
# Environment
ENVIRONMENT=development  # development, staging, production

# Database
DATABASE_URL=sqlite:///data/nhl.db
# DATABASE_URL=postgresql://user:pass@localhost:5432/nhl

# API
NHL_API_BASE_URL=https://api-web.nhle.com/v1
NHL_API_TIMEOUT=30

# Cache
REDIS_URL=redis://localhost:6379/0
CACHE_ENABLED=true
CACHE_TTL=3600

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/nhl.log

# Security (if needed)
SECRET_KEY=your-secret-key-here
API_KEY=your-api-key-if-needed

# Features
ENABLE_ML_PREDICTIONS=false
ENABLE_REAL_TIME_UPDATES=false
```

## Loading Configuration

### In Python Code
```python
from src.utils.config import get_config

# Load configuration based on ENVIRONMENT variable
config = get_config()

# Access configuration values
db_url = config.database.url
api_timeout = config.api.timeout
log_level = config.logging.level
```

### Configuration Priority
1. Environment variables (highest priority)
2. `.env` file
3. Environment-specific YAML file (development.yaml, production.yaml)
4. Default values in code (lowest priority)

## Security Best Practices

### DO NOT commit sensitive data
- Add `.env` to `.gitignore`
- Use `.env.example` as a template
- Store secrets in environment variables or secret management systems
- Never hardcode passwords or API keys

### Sensitive Information
Keep these out of version control:
- Database passwords
- API keys and tokens
- Secret keys
- Private certificates
- User credentials

### Use Environment Variables for Secrets
```python
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
API_KEY = os.getenv("NHL_API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
```

## Configuration Management Tools
- **python-dotenv**: Load environment variables from `.env` file
- **pydantic-settings**: Type-safe configuration with validation
- **PyYAML**: Parse YAML configuration files
- **configparser**: Parse INI-style configuration files

## Example: Type-Safe Configuration
```python
from pydantic_settings import BaseSettings

class DatabaseConfig(BaseSettings):
    url: str
    pool_size: int = 10
    echo: bool = False

class APIConfig(BaseSettings):
    base_url: str
    timeout: int = 30
    rate_limit: int = 100

class AppConfig(BaseSettings):
    database: DatabaseConfig
    api: APIConfig
    
    class Config:
        env_file = ".env"
        env_nested_delimiter = "__"

# Usage
config = AppConfig()
print(config.database.url)
```
