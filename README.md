# Python Clicker Game

## Overview

Very simple, interactive clicker game built with Python, featuring a graphical user interface powered by the `tkinter` package. The game allows players to earn points by clicking, purchase auto-clickers, and unlock achievements. 

## Gameplay

In this game, players earn points by clicking a button with the cursor or by pressing the spacebar. As points accumulate, players can purchase auto-clickers, which automatically generate points. The game also features two clicking modes and unlockable achievements.


## Running the Program (Linux)

### Prerequisites:
- Python 3.8 or higher
- Pillow library

### Steps:
1. Install Python 3.8:
   ```bash
   sudo apt-get update
   sudo apt-get install python3.8
   ```

2. Install the Pillow module:
   ```bash
   sudo apt-get install python3-pillow
   ```

   If you encounter issues with `ImageTk`, use the following command:
   ```bash
   sudo apt-get install python3-pil python3-pil.imagetk
   ```

3. Clone the repository:
   ```bash
   git clone https://github.com/levante00/Python_Project.git
   ```

4. Run the game:
   ```bash
   cd Python_Project
   python3 main.py
   ```



## Project Structure

- `/src`: Contains the main game logic files
- `/Data`: Contains images and other resources used in the game
- `main.py`: Entry point to run the game, links to `src/Play.py`
- `src/Play.py`: Contains the core game code
