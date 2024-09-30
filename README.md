# Sudoku Solver with GUI

This is a simple Sudoku solver game implemented in Python using the Pygame library. It features a graphical user interface (GUI) that allows the user to play Sudoku and solve puzzles automatically using a backtracking algorithm.

## Features
- Play Sudoku with an interactive GUI.
- Automatically solve the Sudoku puzzle using backtracking.
- Enter numbers manually or let the solver complete the puzzle for you.
- Visual feedback for correct and incorrect moves.
- Time tracking and strike system for wrong attempts.

## Demo
![Sudoku GUI](https://github.com/amann-sharma/sudoku-solver/issues/1#issue-2557575051)


## How It Works
- **Backtracking Algorithm**: The program uses a recursive backtracking algorithm to solve the Sudoku puzzle.
- **User Input**: You can enter numbers by selecting a cell and pressing the corresponding number key.
- **Hints**: You can sketch numbers in a cell before confirming the final value.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/amann-sharma/sudoku-solver.git
   ```
2. Navigate to the project directory:
   ```bash
   cd sudoku-solver
   ```
3. Install the required dependencies:
   ```bash
   pip install pygame
   ```
4. Run the application:
   ```bash
   python sudoku_gui.py
   ```

## How to Play
- **Move the mouse** to select a cell.
- **Press a number (1-9)** to sketch a number in the selected cell.
- **Press ENTER** to confirm the number in the cell.
- **Press DELETE** to clear a number.
- **Press SPACE** to let the program automatically solve the Sudoku puzzle.

## Files
- `sudoku_gui.py`: The main program that handles the game logic and user interaction.
- `solver.py`: Contains the Sudoku solver algorithm functions such as `find_empty` and `valid`.

## Future Enhancements
- Add different difficulty levels.
- Implement a hint system.
- Include sound effects and animations.

## Requirements
- Python 3.x
- Pygame

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [Pygame](https://www.pygame.org/) for providing the graphical framework.
```

