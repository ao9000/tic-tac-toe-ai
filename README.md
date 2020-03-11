# Tic Tac Toe with Minimax AI
This project is the implementation of the game Tic Tac Toe with Minimax AI in Python.

## Motivation
After losing to my friend in Tic Tac Toe several times and getting made fun of, I had the idea of developing an unbeatable bot to help me get my sweet revenge.
I thought that a computer bot will have the computational power to run through every single possible move available to find the best move in every scenario, essentially making it unbeatable.

## Screenshots
### Run.py
Text based implementation of the game
![Alt text](images/run.png?raw=true "Tic Tac Toe in command prompt/terminal")

### Run_game.py
GUI (Pygame) implementation of the game
![Alt text](images/run_game.png?raw=true "Selection scene")
![Alt text](images/run_game2.png?raw=true "Game board scene")

## Core tech/framework used
- Minimax AI

Used recursively to derive the best possible move

- Pygame

Used to build the user interface of the game

-Pyinstaller

Used to package the game into an executable file

## Getting started
Follow the steps in order below

### Prerequisites
You will need to have these installed before doing anything else
- Python- 3.8.1 and above ```https://www.python.org/downloads/```
 
### Installation
- Installing Python packages
```
# cd into the root folder of the project
# Change the path accordingly to your system
cd /home/tic-tac-toe-ai

# You should have pip installed as it comes with installing Python
# Installing python packages
pip install -r requirements.txt
```

## Usage

- Text based Tic Tac Toe game
```
# Make sure your in the root directory of the project
python run.py
```

- GUI (Pygame) based Tic Tac Toe game
```
# Make sure your in the root directory of the project
python run_game.py
```

- Test Minimax speed
```
# Make sure your in the root directory of the project
python test_minimax_speed.py
```

- Test Minimax output
```
# Make sure your in the root directory of the project
pytest -vv
```
