## Conways Game of Life - Christmas Edition

![Game Screenshot](/images/game_screen.png)

The Game of Life is a two dimensional universe in which patterns evolve through time. It is a great example of how in science a few simple rules can result in incredibly complex behaviour. 

The Rules in the game are very simple. A square grid contains cells that are either alive or dead. The behaviour of each cell is dependent only on the state of its eight immediate neighbours, according to the following rules:

1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The game was conceptualized by the British mathematician John Horton Conway in the 1970s using pen and paper. The amazing patterns created in it has inspired reasearch in many a computer scientists and helped launch a new branch of mathematics called cellular automata. We hope to re-introduce and inspire a new generation of young computer scientists.

Read more about the game here https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

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

* **gol.py** - This is the entry point of the program, it controls inputs from the user and is responsible for drawing the game on the terminal

* **model.py** - All the logic for applying the different Game of Life Rules and Keeping track of the state of each cell are managed here. 

* **initializer.py** - Initializers contain different shapes, which can be used to initialize the Game of Life grid, when it starts up.

### Modifying the Program

This software is open source software. We hope that you will take this code, own it, change it and reshare with the community. 

Here are some ideas you can try:

* **Modify the rules to implement HighLife https://en.wikipedia.org/wiki/Highlife_(cellular_automaton)**


* **Change the colors**

Change the colors or blocks in the program


* **Create other shapes**

https://en.wikipedia.org/wiki/Still_life_(cellular_automaton)
https://en.wikipedia.org/wiki/Oscillator_(cellular_automaton)


* **Use a sparser memory structure**

The current game uses a an array to store game state. This design uses a lot of memory if the board is large. 
Instead, you could use a sparse memory structure to store state

### Questions

Email us at mmathew 'at'  kenzan.com



