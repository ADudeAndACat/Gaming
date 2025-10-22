# Analytics Module

This module contains data analysis engines and statistical computations.

## Purpose
- Perform statistical analysis on NHL data
- Calculate advanced metrics (Corsi, Fenwick, PDO, xG)
- Generate insights and trends
- Support predictive modeling
- Enable comparative analysis

## Analysis Modules (to be created)
- `player_stats.py` - Player performance analytics and metrics
- `team_stats.py` - Team performance analytics and aggregations
- `predictions.py` - Machine learning models for predictions
- `trends.py` - Trend detection and pattern analysis
- `comparisons.py` - Player vs player, team vs team comparisons

## Analysis Types

### Player Analytics
- Career progression tracking
- Hot/cold streak detection
- Position-specific metrics
- Advanced statistics (Corsi, Fenwick, PDO)

### Team Analytics
- Win/loss patterns
- Home vs away performance
- Special teams efficiency
- Offensive/defensive ratings

### Predictive Analytics
- Game outcome predictions
- Player performance forecasting
- Playoff probability calculations

## Usage Example
```python
from src.analytics.player_stats import PlayerAnalytics

analytics = PlayerAnalytics()
stats = analytics.get_player_season_stats(player_id=8478402, season="20242025")
trends = analytics.detect_hot_streak(player_id=8478402, last_n_games=10)
```

## Dependencies
- pandas for data manipulation
- numpy for numerical computations
- scipy for statistical functions
- scikit-learn for ML models (optional)
