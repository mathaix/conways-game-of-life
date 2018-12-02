
import random

class Initializer(object):
  def __init__(self, gol):
    self.gol = gol

class Toad(Initializer):
  def initialize(self):
      """ Randomly pick a point that fits the shape within the bounds of the Grid  """
      i = random.randint(0,self.gol.x-4)
      j = random.randint(0,self.gol.y-3)

      self.gol.set_cellState(i+1,j,1)
      self.gol.set_cellState(i+2,j,1)
      self.gol.set_cellState(i+3,j,1)
      self.gol.set_cellState(i,j+1,1)
      self.gol.set_cellState(i+1,j+1,1)
      self.gol.set_cellState(i+2,j+1,1)

  @staticmethod
  def desc():
      return "Toad"

class Behive(Initializer):
  def initialize(self):
      """ Randomly pick a point that fits the shape within the bounds of the Grid  """
      i = random.randint(0,self.gol.x-4)
      j = random.randint(0,self.gol.y-3)

      self.gol.set_cellState(i+1,j,1)
      self.gol.set_cellState(i+2,j,1)
      self.gol.set_cellState(i,j+1,1)
      self.gol.set_cellState(i+3,j+1,1)
      self.gol.set_cellState(i+1,j+2,1)
      self.gol.set_cellState(i+2,j+2,1)

  @staticmethod
  def desc():
      return "Behive"

class Glider(Initializer):
  def initialize(self):
      """ Randomly pick a point that fits the shape within the bounds of the Grid  """
      i = random.randint(0,self.gol.x-4)
      j = random.randint(0,self.gol.y-3)

      self.gol.set_cellState(i,j,1)
      self.gol.set_cellState(i+2,j,1)
      self.gol.set_cellState(i+1,j+1,1)
      self.gol.set_cellState(i+2,j+1,1)
      self.gol.set_cellState(i+1,j+2,1)

  @staticmethod
  def desc():
      return "Glider"

class Random(Initializer):
  def initialize(self):
      """ Randomly initializes Grid with shapes"""

      shapes = [Behive, Toad, Glider]

      for i in range(10):
        shape = shapes[random.randint(0,len(shapes)-1)]
        shape(self.gol).initialize()

  @staticmethod
  def desc():
      return "Random"

initializers = {
            'g' : Glider, 
            'b' : Behive, 
            't' : Toad,
            'r' : Random
        }