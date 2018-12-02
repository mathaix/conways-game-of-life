## Conways Game of Life - Christmas Edition

The Game of Life is a two dimensional universe in which patterns evolve through time. It is a great example of how in science a few simple rules can result in incredibly complex behaviour. 

The Rules in the game are very simple. A square grid contains cells that are either alive or dead. The behaviour of each cell is dependent only on the state of its eight immediate neighbours, according to the following rules:

1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

You can read more about the game here https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

It was invented by the British mathematician John Horton Conway in the 1970 and helped launch a new branch of mathematics called cellular automata

### Running the Program

Note this program may not run on windows

1. First install Python3 . Python 3 can be download and installed from here https://www.python.org/downloads/
2. Download the code
   Code can be downloaded by either
   a) Downloading the code directly ()
   
   b) Cloning the repository. 
      First Install git https://www.atlassian.com/git/tutorials/install-git
      Clone the repository:
        git clone https://github.com/kenzanlabs/conways-game-of-life.git
        
3. cd into the folder where the files are located
   cd conways-game-of-life
   
4. Install required libraries 
   pip install urwid
   
5. Run the program
   python gol.py

### Program Design

The program consists of 3 files. 
gol.py - This is the entry point of the program, it controls inputs from the user and is responsible for drawing the game on the terminal

model.py - All the logic for applying the different Game of Life Rules and Keeping track of the state of each cell are managed here. 

initializer.py - Initializers contain different shapes, which can be used to initialize the Game of Life grid, when it starts up.

### Modifying the Program
