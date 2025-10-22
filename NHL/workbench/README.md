# Workbench - Prototyping & Experimentation Area

This is your **self-contained workspace** for prototyping, experimenting, and playing with different aspects of the NHL analytics system during development.

## Purpose
- **Rapid prototyping** without affecting main codebase
- **Experiment** with new ideas, APIs, and algorithms
- **Test** different approaches before implementation
- **Learn** and explore NHL data interactively
- **Sandbox** for trying out new libraries and techniques

## Subdirectories

### experiments/
Quick experiments and proof-of-concepts:
- Testing NHL API endpoints
- Trying new visualization libraries
- Exploring data structures
- Performance benchmarking
- Algorithm prototypes

**Example files:**
- `test_nhl_api.py` - Quick API endpoint tests
- `plotly_vs_matplotlib.py` - Compare visualization libraries
- `query_performance.py` - Test database query speeds

### prototypes/
More developed prototypes of features:
- Feature prototypes before integration
- Alternative implementations
- Proof-of-concept applications
- Mini-projects

**Example files:**
- `shot_chart_prototype.py` - Working shot chart visualization
- `prediction_model_v1.py` - First attempt at ML predictions
- `dashboard_mockup.py` - Dashboard layout prototype

### sandbox/
Free-form experimentation and learning:
- Learning new libraries
- Playing with data
- Throwaway code
- Quick tests
- Random ideas

**Example files:**
- `play_with_pandas.py` - Learning pandas operations
- `test_ideas.py` - Random code snippets
- `scratch.py` - Temporary workspace

## Usage Guidelines

### Freedom to Experiment
- **No rules**: Write messy code, it's okay!
- **No tests required**: Focus on exploration
- **No documentation needed**: Comments optional
- **No code review**: This is your personal space
- **Commit or don't**: Up to you

### When to Graduate Code
Move code from workbench to main codebase when:
1. Prototype proves successful
2. Code is cleaned up and tested
3. Feature is ready for integration
4. Implementation is stable

### File Naming
Use descriptive names with dates:
- `2024-10-22_api_exploration.py`
- `shot_chart_v1.py`, `shot_chart_v2.py`
- `experiment_corsi_calculation.py`

### Keep It Organized
- Delete old experiments periodically
- Archive successful prototypes
- Document key findings in comments
- Note what worked and what didn't

## Example Workflow

### 1. Quick API Test
```python
# workbench/experiments/test_standings_api.py
import requests
import json

# Quick test of standings endpoint
response = requests.get("https://api-web.nhle.com/v1/standings/now")
data = response.json()

print(json.dumps(data, indent=2))
print(f"Found {len(data.get('standings', []))} teams")
```

### 2. Prototype a Feature
```python
# workbench/prototypes/player_comparison.py
"""
Prototype: Compare two players' statistics
Goal: Test approach before implementing in src/analytics/
"""
import pandas as pd

def compare_players(player1_id, player2_id):
    # Fetch player data
    # Calculate comparison metrics
    # Generate visualization
    pass

if __name__ == "__main__":
    # Test with Connor McDavid vs Auston Matthews
    compare_players(8478402, 8479318)
```

### 3. Experiment in Sandbox
```python
# workbench/sandbox/play_with_plotly.py
# Just learning how plotly works
import plotly.graph_objects as go

fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
fig.show()

# Try different chart types
# Test interactivity
# Explore styling options
```

## Tips for Effective Prototyping

### Start Small
- Test one thing at a time
- Use small datasets first
- Build incrementally
- Validate assumptions early

### Document Findings
Add comments about what you learned:
```python
# FINDINGS:
# - NHL API rate limit seems to be ~100 req/min
# - Standings endpoint returns current date by default
# - Team abbreviations are 3 letters (TOR, MTL, etc.)
# - Response time averages 200ms
```

### Save Successful Patterns
When you find something that works well:
```python
# THIS WORKS WELL - Consider moving to src/utils/
def parse_nhl_date(date_string):
    """Converts NHL API date format to datetime."""
    # Implementation that works
    pass
```

### Track Iterations
Keep versions of evolving prototypes:
- `shot_chart_v1.py` - Basic implementation
- `shot_chart_v2.py` - Added heat map
- `shot_chart_v3.py` - Final version (ready to move to src/)

## Integration Checklist

Before moving code from workbench to main codebase:
- [ ] Clean up code and remove debug statements
- [ ] Add proper error handling
- [ ] Write docstrings and type hints
- [ ] Create unit tests
- [ ] Follow project coding standards
- [ ] Update relevant documentation
- [ ] Remove hardcoded values
- [ ] Add logging instead of print statements

## Examples of What to Prototype Here

### API Exploration
- Test all NHL API endpoints
- Understand response formats
- Find rate limits
- Discover undocumented features

### Data Analysis
- Explore statistical relationships
- Test different metrics
- Validate data quality
- Find interesting patterns

### Visualizations
- Try different chart types
- Test color schemes
- Experiment with layouts
- Compare libraries

### Algorithms
- Test prediction models
- Try different approaches
- Benchmark performance
- Validate accuracy

### Tools & Libraries
- Learn new packages
- Compare alternatives
- Test compatibility
- Evaluate performance

## Workbench vs Notebooks

**Use Workbench when:**
- Writing Python scripts
- Building prototypes
- Testing implementations
- Quick experiments

**Use Notebooks when:**
- Interactive data exploration
- Step-by-step analysis
- Creating reports
- Sharing findings

Both are valid! Use what works best for your workflow.

---

**Remember**: The workbench is YOUR space. Experiment freely, break things, learn, and have fun! 🚀
