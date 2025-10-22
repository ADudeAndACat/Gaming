# Notebooks Directory

This directory contains Jupyter notebooks for data exploration and analysis.

## Purpose
- Explore NHL data interactively
- Prototype analytics and visualizations
- Document analysis workflows
- Share findings and insights
- Create reproducible research

## Subdirectories

### exploratory/
Notebooks for initial data exploration and discovery:
- Understanding API responses
- Exploring data distributions
- Finding patterns and anomalies
- Testing hypotheses
- Quick prototyping

### analysis/
Notebooks for in-depth analysis and reporting:
- Season analysis reports
- Player performance studies
- Team comparison analyses
- Statistical modeling
- Publication-ready visualizations

## Naming Convention
Use descriptive names with dates:
- `2024-10-22_initial_api_exploration.ipynb`
- `2024-10-23_player_scoring_trends.ipynb`
- `2024-10-24_team_performance_analysis.ipynb`

## Best Practices

### Organization
- One notebook per analysis topic
- Clear markdown documentation
- Logical section headers
- Summary at the top

### Code Quality
- Import all dependencies at the top
- Define reusable functions
- Add comments for complex logic
- Clean up outputs before committing

### Reproducibility
- Set random seeds where applicable
- Document data sources and versions
- Include environment requirements
- Save key outputs (figures, tables)

## Example Notebook Structure
```python
# Title: Player Scoring Trends Analysis
# Date: 2024-10-22
# Author: Your Name

## 1. Setup
import pandas as pd
import plotly.express as px
from src.database.connection import get_session
from src.analytics.player_stats import PlayerAnalytics

## 2. Load Data
# Description of data being loaded
...

## 3. Exploratory Analysis
# Initial exploration and visualizations
...

## 4. Key Findings
# Summary of insights
...

## 5. Next Steps
# Future work and questions
...
```

## Running Notebooks
```bash
# Start Jupyter Lab
jupyter lab

# Start Jupyter Notebook
jupyter notebook

# Convert notebook to script
jupyter nbconvert --to script notebook.ipynb

# Convert notebook to HTML
jupyter nbconvert --to html notebook.ipynb
```

## Tips
- Use notebooks for exploration, move production code to modules
- Restart kernel and run all cells before sharing
- Export important visualizations as images
- Consider using nbstripout to remove outputs from git
