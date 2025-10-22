# Tests Directory

This directory contains all test suites for the NHL analytics system.

## Purpose
- Ensure code quality and correctness
- Prevent regressions
- Document expected behavior
- Enable confident refactoring

## Test Structure
- `unit/` - Unit tests for individual functions and classes
- `integration/` - Integration tests for module interactions
- `fixtures/` - Test data and fixtures (sample API responses, mock data)

## Test Organization
Mirror the source code structure:
```
tests/
├── unit/
│   ├── test_api_client.py
│   ├── test_collectors.py
│   ├── test_database_models.py
│   ├── test_analytics.py
│   └── test_visualizations.py
├── integration/
│   ├── test_data_pipeline.py
│   ├── test_api_to_database.py
│   └── test_end_to_end.py
└── fixtures/
    ├── sample_game_response.json
    ├── sample_player_data.json
    └── mock_database.py
```

## Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/unit/test_api_client.py

# Run tests matching pattern
pytest -k "test_player"

# Run with verbose output
pytest -v
```

## Writing Tests
```python
import pytest
from src.api.client import NHLAPIClient

class TestNHLAPIClient:
    @pytest.fixture
    def client(self):
        return NHLAPIClient()
    
    def test_get_teams(self, client):
        teams = client.get_teams()
        assert len(teams) > 0
        assert teams[0].name is not None
    
    @pytest.mark.asyncio
    async def test_async_fetch(self, client):
        result = await client.fetch_async("/teams")
        assert result is not None
```

## Test Coverage Goals
- Aim for >80% code coverage
- 100% coverage for critical paths (data collection, database operations)
- Test edge cases and error conditions
- Mock external API calls in unit tests

## Testing Tools
- pytest - Testing framework
- pytest-asyncio - Async test support
- pytest-cov - Coverage reporting
- pytest-mock - Mocking utilities
- faker - Generate test data
- responses - Mock HTTP requests
