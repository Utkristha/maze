from graphics import *
from maze import * 
import pygame

pygame.init()


temp_graphics = maze_creation(1, [])
maze_size = temp_graphics.start_screen()

if maze_size is None:
    exit()


m2 = maze_algo(maze_size)
m2.maze_generation()
grid = m2.get_grid()
maze = maze_creation(maze_size, grid)


while maze.running:
    maze.grid_maker()

    if maze.start_pos and maze.end_pos:
        m2.solve_maze(maze.start_pos, maze.end_pos)

pygame.quit()
