# Hangman Game

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/) [![Status](https://img.shields.io/badge/status-prototype-orange.svg)]()

A simple command-line Hangman game in Python. Before your game begins, the computer randomly chooses a word for the player to guess. The game displays the mystery word as a series of asterisks ("*") and the player has a certain number of guesses to guess letters. The player wins if they guess the word before they run out of guesses.

## Features
- Fetches a random word using the `random-word` package
- Reveals correctly guessed letters and shows attempts left
- Tracks letters guessed

## Requirements
- Python 3.8+
- `random-word` Python package

## Installation
1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
.
```

2. Install dependencies:

```bash
pip install random-word
```

## Running
Run the game from the project root:

```bash
python "main.py"
```

## License
This project is licensed under the terms in the [LICENSE](LICENSE) file.
