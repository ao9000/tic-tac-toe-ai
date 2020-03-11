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

## Core framework/concepts used
- Minimax with Alpha-beta pruning

Minimax is an artificial intelligence (AI) algorithm used in 2-player decision based board games such as Tic Tac Toe, Checkers and Chess.
Minimax algorithm performs well on perfect information games where both players are informed about the previous and possible future moves of the player.
Perfect information games provides the algorithm the ability to predict future moves made by the opponent.
The well-informed algorithm then can execute a counter-play to whatever move the opponent decides to take.

However, Minimax by itself is very slow, even in the game of Tic Tac Toe that only has a maximum of 9 possible moves.
After all, the algorithm is running through all of the possible moves and calculating the best move against it.
Keeping in mind that every possible move opens up another set of possible moves, the algorithm will take the longest to compute at the early stages of the game and will slowly gain speed towards the mid and late stages of the game.
To avoid waiting for an average of 10 seconds every time the game starts, this is where Alpha-beta pruning comes in.
Alpha-beta pruning eliminates paths in the decision tree that are guaranteed to do worse than the alternate paths.
Thus, saving time computing by skipping the branches altogether.

- Numpy arrays

Using Numpy arrays instead of Python list provides some computational speed boost and memory optimization.

- Pygame

Using pygame to build the graphical user interface (GUI) for the Tic Tac Toe game.

- Pyinstaller

Used to package the pygame into an executable file to facility easy distribution.

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

## References
Sources that I took reference during development

Lague, S. (2018). Algorithms Explained – minimax and alpha-beta pruning. YouTube. Retrieved 11 March 2020, from https://youtu.be/l-hh51ncgDI.

Pygame Front Page — pygame v2.0.0.dev5 documentation. Pygame.org. Retrieved 11 March 2020, from https://www.pygame.org/docs/.

PyInstaller Manual — PyInstaller 3.6 documentation. Pyinstaller.readthedocs.io. Retrieved 11 March 2020, from https://pyinstaller.readthedocs.io/en/stable/index.html.

Python Lists vs. Numpy Arrays - What is the difference?: IST Advanced Topics Primer. Webcourses.ucf.edu. Retrieved 11 March 2020, from https://webcourses.ucf.edu/courses/1249560/pages/python-lists-vs-numpy-arrays-what-is-the-difference.
