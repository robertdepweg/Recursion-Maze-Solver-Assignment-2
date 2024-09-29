# Author: Robert Depweg
# Class: CIS226
# Date: 9/28/24
"""Maze Solver Module"""

# First-party imports
from colors import print_o, print_x

class MazeSolver:
    """This class is used for solving a 2d list maze.

    You might want to add other methods to help you out.
    A print maze method would be very useful, and probably necessary to print the solution.
    If you are real ambitious, you could make a separate class to handle that."""

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

        print()
        print("First maze is finished!")

    def _maze_traversal(self, maze, current_x, current_y):
        """Traverses the maze by recursion"""

        # Changes period to X if need be
        if maze[current_x][current_y] == '.':
            maze[current_x][current_y] = 'X'
            # Calls seperate function to print the maze
            self.print_maze(maze)
            
        # Base case: checks current position to see if exit reached
        if (current_x + 1) == len(maze) or (current_y + 1) == len(maze):
            self.finish_flag = True

        # Check down
        if maze[current_x + 1][current_y] == '.' and self.finish_flag != True:
            self._maze_traversal(maze, current_x + 1, current_y)
        # Check up
        if maze[current_x - 1][current_y] == '.' and self.finish_flag != True:
            self._maze_traversal(maze, current_x - 1, current_y)
        # Check left
        if maze[current_x][current_y - 1] == '.' and self.finish_flag != True:
            self._maze_traversal(maze, current_x, current_y - 1)
        # Check right
        if maze[current_x][current_y + 1] == '.' and self.finish_flag != True:
            self._maze_traversal(maze, current_x, current_y + 1)
        # Changes to O if at dead end or wrong path
        maze[current_x][current_y] = 'O'
        self.print_maze(maze)
        
    def print_maze(self, maze):
        """Prints the maze for each step taken"""
        for y in maze:
            print()
            for symbol in y:
                if symbol == 'X':
                    print_x(symbol)
                elif symbol == 'O':
                    print_o(symbol)
                else:
                    print(symbol, end=" ")
