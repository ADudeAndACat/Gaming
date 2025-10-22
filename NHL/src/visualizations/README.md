# Visualizations Module

This module generates charts, graphs, and interactive visualizations.

## Purpose
- Create static and interactive visualizations
- Generate publication-quality charts
- Build reusable visualization components
- Export visualizations in various formats

## Visualization Modules (to be created)
- `charts.py` - Standard charts (line, bar, scatter, box plots)
- `dashboards.py` - Dashboard layouts and compositions
- `heatmaps.py` - Heat maps and spatial visualizations (shot charts)
- `reports.py` - Report generation with multiple visualizations

## Visualization Types

### Standard Charts
- Line charts for trends over time
- Bar charts for comparisons
- Scatter plots for correlations
- Box plots for distributions

### Interactive Dashboards
- Team performance dashboard
- Player comparison tool
- League-wide statistics
- Live game tracker

### Specialized Visualizations
- Shot charts (heat maps on ice rink)
- Ice rink visualizations
- Network graphs (passing patterns)
- Geographic maps (player origins)

## Usage Example
```python
from src.visualizations.charts import create_player_trend_chart
from src.visualizations.heatmaps import create_shot_chart

# Create a line chart of player goals over time
fig = create_player_trend_chart(player_id=8478402, metric="goals")
fig.show()

# Create a shot chart heat map
shot_chart = create_shot_chart(game_id=2024020001, team_id=10)
shot_chart.save("shot_chart.png")
```

## Technologies
- Plotly for interactive web-based charts
- Matplotlib/Seaborn for static publication-quality charts
- Pillow for image manipulation
- ReportLab or WeasyPrint for PDF reports
