import random
import initializer

#
#  Game of Life Class. 
#  Encapsulates all the functionality to transition to a new state from 
#  the current state based on the Game of Life Rules
#  The class gets called from the Game Controller Controller
#  
#  See https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
#
class GameofLife(object):   
    # Initialize the Game with Dimensions of the View Area
    def __init__(self, x, y, initializer_key=None):
        if x % 2 == 0:
          self.x = int(x/2)
        else:
            self.x = int(x/2) + 1
        self.y = y
        self.data = [0]* self.x * self.y    # State of each cell is stored in Array of size x*y. 
        
        if initializer_key:
            initializer.initializers[initializer_key](self).initialize()

    # Traverse each point in the grid and update each cell
    def update(self):
        # Capture state changes in a temporary buffer, because updating self.data directly 
        # will affect how transitions are applied
        buffer = [0]* self.x * self.y  
        for i in range(self.x):
            for j in range(self.y):
              self.live_or_die(buffer, i, j)        
        self.data = buffer

    # Apply the following rules to a cell and decide if it need to live or die
    # 
    # Any live cell with fewer than two live neighbors dies, as if by underpopulation.
    # Any live cell with two or three live neighbors lives on to the next generation.
    # Any live cell with more than three live neighbors dies, as if by overpopulation.
    # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    def live_or_die(self, data, i, j):
        neighbour_count = self.get_neighbours(i, j)
        self.set_cell_state(data, i, j, self.get_cell_state(i,j))
        if self.get_cell_state(i, j) == 1:
          if neighbour_count < 2 or neighbour_count > 3:
              self.set_cell_state(data,i,j,0)
        else:
          if neighbour_count == 3:
           self.set_cell_state(data,i,j,1)    

    # Set the state of a cell in the current grid (helper function for the initializers)
    def set_cellState(self, i, j, value):
        self.set_cell_state(self.data, i, j, value)
        
    # Set the state of a cell in a grid
    def set_cell_state(self, data, i, j, value):
        data[self._get_index(i,j)] = value

    # Get the state of a cell, ie if it is alive or dead
    def get_cell_state(self, x, y):
        return self.data[self._get_index(x,y)]

    #
    # Helper function to index into the Array
    # Index is done in a way so as to wrap around the grid
    #
    def _get_index(self, x, y):
        if x < 0: x = self.x - 1 
        if x >= self.x: x = 0
        if y < 0: y = self.y - 1
        if y >= self.y: y = 0
        return self.x  * y + x

    # tranform the grid, setting attributes so that colors are set
    def get_data(self):
        return [self.render_alive_cell() if x is 1  else ('black','. ') for x in self.data]

    def render_alive_cell(self):
        symbols = ['▨ ', '▩ ']
        colors = ['green', 'greenl','yellow','red']
        return (random.choice(colors), random.choice(symbols))

    # Get number of alive cells next to the current cell           
    def get_neighbours(self, x, y):
        return  self.get_cell_state( x - 1 , y - 1) + \
                self.get_cell_state( x  , y - 1) +  \
                self.get_cell_state( x + 1 , y - 1) + \
                self.get_cell_state( x - 1 , y ) +  \
                self.get_cell_state( x + 1 , y ) +  \
                self.get_cell_state( x - 1 , y  + 1) + \
                self.get_cell_state( x  , y + 1) +  \
                self.get_cell_state( x + 1 , y + 1)

    def get_initialize_text(self):
        initializer_text = []
        for key, value in initializer.initializers.items(): 
            initializer_text.append ("%s for %s" % (key,value.desc()))

        initializer_text.append('and q to Quit')
        return 'Press: ' + ', '.join(initializer_text)

    def get_initialize_keys(self):
        return [key for key in initializer.initializers.keys()]
