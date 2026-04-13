Markdown
# 🔴🔵 Four in a Row (Connect 4)

A classic local 2-player Connect 4 game built with Python and Pygame. 

*Fun fact: This project was originally written in Python 2.7 almost a decade ago and has recently been revived, dusted off, and updated to run smoothly on modern Python 3!*

## 🛠️ Requirements

To run this game, you will need **Python 3** and the Pygame Community Edition library. 

1. Install [Python](https://www.python.org/downloads/) (Make sure to check "Add Python to PATH" during installation).
2. Install Pygame-CE by running this command in your terminal:
   ```bash
   py -m pip install pygame-ce
🚀 How to Run
Clone or download this repository.

Open your terminal and navigate to the project folder.

Run the main script:

Bash
py main.py
(On Mac/Linux, use python3 main.py)

🎮 How to Play
The game randomly selects who goes first (Player 1 is Red, Player 2 is Blue).

Use your mouse to click on the column where you want to drop your token.

The first player to connect 4 tokens in a row (horizontally, vertically, or diagonally) wins!

Press ESC or click the X on the window to close the game.

📁 File Structure Overview
main.py - The main game loop, event handling, and window rendering.

board.py - The game board logic, handling token placement and state.

token.py - Logic for the individual tokens on the board.

*.png / *.jpg - Game assets, buttons, and win screens.