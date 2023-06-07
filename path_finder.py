import pygame
import math
# Python queue is a linear abstract data structure that follows the first in-first out (FIFO) approach
from queue import PriorityQueue


# set display
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path Finding Algo")

# const
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# visualization yool
# spot = cube
class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
        
    # position
    def get_pos(self):
        return self.row, self.col
    
    def is_closed(self):
        return self.color == RED
    
    def is_open(self):
        return self.color == GREEN
    
    def is_barrier(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == PURPLE
    
    def reset(self):
        self.color == WHITE
        
    def make_close(self):
        self.color== RED
        
    def make_open(self):
        self.color  == GREEN
        
    def make_barrier(self):
        self.color == BLACK
        
    def make_end(self):
        self.color == TURQUOISE
        
    def make_path(self):
        self.color = PURPLE
        
    def draw(self, win):
        pygame.draw.rect(win, self.color, ())