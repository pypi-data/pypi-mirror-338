# TrueRoll: Ten-Pin Bowling Simulation

TrueRoll is an extensive simulation toolkit designed for modeling ten-pin bowling games. It offers a comprehensive suite of classes that simulate games, tournaments, leagues, and more, providing a realistic and detailed representation of bowling dynamics. The project also includes a scoring system compatible with various bowling rules, a database for persisting game results, and multiple interfaces (CLI, TUI, Web) for interacting with the library.

## Features

- **Simulation Classes**: Simulate bowling games frame by frame or as complete games using different probabilities for strikes, spares, and opens.
- **Scoring Systems**: Includes traditional, current frame, and 9-pin no-tap scoring systems.
- **Bowling Database**: A SQLite database integration for storing and managing bowling games, bowlers, alleys, and tournaments.
- **League and Tournament Support**: Organize and run bowling tournaments and leagues with multiple games and multiple bowlers, customizable for different team sizes and frequencies.
- **Multiple Interfaces**:
  - **Command Line Interface (CLI)**: Using Typer for a rich command-line experience
  - **Terminal User Interface (TUI)**: Using Textual for an interactive terminal application
  - **Web Interface**: Using FastHTML for a modern, responsive web application
- **Documentation**: Auto-generated API documentation using MkDocs for easy reference and usage.

## Installation

### Using pip

```bash
pip install trueroll
```

### From source

Clone the repository and install using pip:

```bash
git clone https://github.com/michael-borck/trueroll.git
cd trueroll
pip install -e .
```

## Usage

### As a Python Library

```python
from trueroll import Bowler, Game, Scoring

# Create a bowler
player = Bowler("John Doe", 180)

# Create a game
game = Game(player)
game.roll(10)  # Strike
game.roll(5)   # 5 pins
game.roll(5)   # Spare

# Get the score
score = Scoring.calculate_score(game)
print(f"{player.name}'s score: {score}")
```

### Command Line Interface (CLI)

TrueRoll provides a command-line interface with various subcommands:

```bash
# Show CLI help
trueroll --help

# Manage bowlers
trueroll bowlers list
trueroll bowlers add "John Doe" 180

# Manage games
trueroll games list
trueroll games add "John Doe" 210

# Start the Terminal UI
trueroll tui start

# Start the Web Interface
trueroll web start
```

### Terminal User Interface (TUI)

Start the interactive terminal interface:

```bash
trueroll tui start
```

Or from Python:

```python
import trueroll
trueroll.run_tui()
```

### Web Interface

Start the web server:

```bash
trueroll web start --host 0.0.0.0 --port 8080
```

Or from Python:

```python
import trueroll
trueroll.run_web(host="0.0.0.0", port=8080, debug=True)
```

Then open your browser at `http://localhost:8080`.

## Documentation

Generate and view the documentation locally:

```bash
# Install development dependencies
pip install "trueroll[dev]"

# Serve the documentation
mkdocs serve
```

## Testing

Run tests using pytest:

```bash
pytest
```

## Contributing

Contributions are welcome! Please read the [contributing guide](docs/contribute.md) for directions on how to submit pull requests to the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.