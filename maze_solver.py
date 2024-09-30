# Author: Robert Depweg
# Class: CIS226
# Date: 9/28/24
"""Maze Solver Module"""

# First-party imports
from colors import print_o, print_x

class MazeSolver:
    """Class that solves a two dimensional maze"""

    def __init__(self):
        """Constructor for MazeSolver"""
        # Bool for finish status
        self.finish_flag = False

    def solve_maze(self, maze, x_start, y_start):
        """Public method that calls private maze solving method"""
        # Holds current coordnates
        current_x = x_start
        current_y = y_start

        # The maze solver
        self._maze_traversal(maze, current_x, current_y)

        # Sets finish flag back after solving is complete
        self.finish_flag = False

        # Prints new line from maze
        print()

    def _maze_traversal(self, maze, current_x, current_y):
        """Traverses the maze by recursion"""
        # Changes period to X if need be
        if maze[current_x][current_y] == '.':
            maze[current_x][current_y] = 'X'
            # Calls seperate function to print the maze
            self.print_maze(maze)
            
        # Base case: checks current position to see if exit reached at edge of maze
        if (current_x + 1) == len(maze) or (current_y + 1) == len(maze):
            self.finish_flag = True

        # Check down
        if self.finish_flag != True and maze[current_x + 1][current_y] == '.':
            self._maze_traversal(maze, current_x + 1, current_y)
        # Check up
        if self.finish_flag != True and maze[current_x - 1][current_y] == '.':
            self._maze_traversal(maze, current_x - 1, current_y)
        # Check left
        if self.finish_flag != True and maze[current_x][current_y - 1] == '.':
            self._maze_traversal(maze, current_x, current_y - 1)
        # Check right
        if self.finish_flag != True and maze[current_x][current_y + 1] == '.':
            self._maze_traversal(maze, current_x, current_y + 1)
        # Changes to O if at dead end or wrong path
        if self.finish_flag != True:
            maze[current_x][current_y] = 'O'
            self.print_maze(maze)
        
    def print_maze(self, maze):
        """Prints the maze for each step taken in corresponding symbol color"""
        for row in maze:
            # Prints new line for every new row
            print()
            for symbol in row:
                # Prints X in green
                if symbol == 'X':
                    print_x(symbol)
                # Prints O in red
                elif symbol == 'O':
                    print_o(symbol)
                # Prints other symbols normally
                else:
                    print(symbol, end=" ")
        # Prints final new line to seperate the different mazes
        print()
