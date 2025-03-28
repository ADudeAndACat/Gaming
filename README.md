# Gaming Utilities

A collection of Python scripts for tabletop gaming, featuring dice simulation and analysis tools.

## Features

### Dice Rolling
- Multiple implementations of dice rolling (functional, OOP, and dictionary-based)
- Support for standard polyhedral dice (d4, d6, d8, d10, d12, d20, d100)
- Roll history tracking with JSON storage
- Modifiers and multiple roll support

### Roll Analysis Dashboard
- Interactive web dashboard using Streamlit
- Statistical analysis of roll history
- Distribution visualizations
- Fairness scoring
- Roll pattern analysis over time

### Other Utilities
- `crafting.py` - Pathfinder crafting calculator
- `heals.py` - Randomizer for 'cure' spell results
- `statsmaker.py` - Character stat generators for Pathfinder and Dungeon Crawl Classics

## Installation

1. Clone this repository

2. Choose your preferred package installation method:

### Using UV (Recommended - Faster Installation)
```bash
# Install UV
pip install uv

# Create and activate virtual environment
uv venv
.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On Unix/MacOS

# Install dependencies
pip install -r requirements.txt
```

### Using pip
```bash
# Create and activate virtual environment
python -m venv venv
.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On Unix/MacOS

# Install dependencies
pip install -r requirements.txt
```

### Using pipenv
```bash
# Install pipenv if you haven't already
pip install pipenv

# Install dependencies
pipenv install

# Activate the environment
pipenv shell
```

### Manual Installation
If you prefer to install packages individually:
```bash
pip install streamlit==1.41.1 pandas==2.2.3 numpy==2.2.0 plotly==5.24.1
```

## Running Tests

The project includes a comprehensive test suite using Python's unittest framework.

### Running All Tests
```bash
# Using the run_tests.py script
python run_tests.py

# Or using unittest directly
python -m unittest discover -s test
```

### Test Structure
- `test/` - Contains all test files
- Each module has a corresponding test file with the naming convention `test_*.py`
- `test/conftest.py` - Contains shared test fixtures and utilities
- `test/test_time.py` - Performance benchmarking tests

## Usage

### Using the Main Interface
The easiest way to use all utilities is through the main interface:
```bash
python main.py
```
This provides an interactive menu to access all features:
1. Dice Rolling - Test different dice rolling implementations
2. Character Stats - Generate character stats for different systems
3. Healing Spells - Calculate healing spell results
4. Crafting - Calculate crafting times and costs
5. Run All Demonstrations - Try everything at once

### Individual Module Usage

#### Dice Rolling
```python
from diceroller import d20, d6

# Roll a d20 with +5 modifier
d20(5)

# Roll 3d6
d6(times=3)

# Using the OOP implementation
from diceroller_class import DiceRoller
d20_roller = DiceRoller(20)
result = d20_roller.roll()
```

#### Character Stats
```python
from statsmaker import makepfstats, makedccstats

# Generate Pathfinder stats
makepfstats()

# Generate DCC stats
makedccstats()
```

#### Healing Calculator
```python
from heals import clw, cmw, csw, ccw

# Cast Cure Light Wounds at level 3
clw(3)

# Cast Cure Critical Wounds at level 9
ccw(9)
```

#### Crafting Calculator
```python
from crafting import crafting

# Calculate crafting (roll=15, DC=20, price=100sp, with Crafter's Fortune)
result = crafting(15, 20, 100, 'y')
```

### Roll Analysis Dashboard
Run the analysis dashboard:
```bash
streamlit run roll_analysis.py
```

## Files

### Core Dice Rolling
- `diceroller.py` - Main functional implementation of dice rolling system
  - Supports all standard polyhedral dice (d4-d100)
  - Includes modifiers and multiple roll support
  - JSON-based roll history tracking

- `diceroller_class.py` - Object-oriented implementation of the dice roller
  - Class-based approach for dice rolling
  - Encapsulated roll logic and history management
  - Same functionality as diceroller.py in OOP style

- `diceroller_dictionary.py` - Dictionary-based implementation
  - Uses lambda functions for dice rolling
  - Lightweight alternative implementation
  - Quick access to different dice types

### Analysis Tools
- `roll_analysis.py` - Interactive Streamlit dashboard for analyzing dice rolls
  - Statistical analysis of roll history
  - Distribution visualizations
  - Roll pattern analysis over time
  - Fairness assessment tools
  - Interactive data filtering and display

- `time_test.py` - Performance testing module
  - Measures execution time of different dice rolling implementations
  - Includes decorators for precise timing
  - Useful for comparing implementation efficiency

### Game Utilities
- `crafting.py` - Pathfinder crafting calculator
  - Calculates crafting costs and time
  - Supports different crafting rules and modifiers

- `heals.py` - Healing spell calculator
  - Randomizes 'cure' spell results
  - Supports different healing spell levels
  - Includes modifiers for healing calculations

- `statsmaker.py` - Character stat generation tools
  - Supports multiple RPG systems:
    - Pathfinder
    - Dungeon Crawl Classics
  - Various stat rolling methods

### Main Interface
- `main.py` - Central entry point for all utilities
  - Interactive menu system
  - Demonstrates all available features
  - Easy access to all functionality
  - Great starting point for new users

### Data Files
- `rolls.json` - Storage file for dice roll history
  - JSON format for easy parsing
  - Stores roll results with timestamps
  - Used by analysis dashboard

### Project Configuration
- `requirements.txt` - Project dependencies
  - Lists all required Python packages
  - Includes version specifications
  - Supports multiple installation methods

## Contributing

Feel free to open issues or submit pull requests with improvements.
