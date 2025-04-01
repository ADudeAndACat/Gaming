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
uv pip install -r requirements.txt
```

### Using pip
```bash
# Create and activate virtual environment
python -m venv .venv
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

## Project Structure

### Core Files
- `config.py` - Central configuration for the package
- `utils.py` - Shared utility functions used across modules
- `main.py` - Main entry point with an interactive menu

### Core Dice Rolling
- `diceroller.py` - Functional implementation of dice rolling system
- `diceroller_class.py` - Object-oriented implementation of the dice roller
- `diceroller_dictionary.py` - Dictionary-based implementation with lambda functions

### Analysis Tools
- `roll_analysis.py` - Interactive Streamlit dashboard for analyzing dice rolls

### Game Utilities
- `crafting.py` - Pathfinder crafting calculator
- `heals.py` - Healing spell calculator
- `statsmaker.py` - Character stat generators

## Future Enhancements

We're planning several enhancements for future versions:

1. **Database Integration** - Replace JSON storage with SQLite for better performance
2. **Web API** - Create a REST API to allow integration with web applications
3. **Expanded Game Systems** - Add support for more RPG systems
4. **Plugin System** - Develop a modular system for extending functionality
5. **User Profiles** - Allow saving of character information and preferences

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
