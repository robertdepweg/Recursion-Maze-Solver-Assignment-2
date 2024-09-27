# Author: Robert Depweg
# Class: CIS226
# Date: 9/24/24
"""Maze Solver Module"""


class MazeSolver:
    """This class is used for solving a 2d list maze.

    You might want to add other methods to help you out.
    A print maze method would be very useful, and probably necessary to print the solution.
    If you are real ambitious, you could make a separate class to handle that."""

    def __init__(self):
        """Constructor for MazeSolver"""

        # NOTE: Though not required, you may want to define some class level
        # variables here that you are able to access and set anywhere during
        # recursion. This is why the init constructor is defined here for you.
        # Holds exit coordnates
        self.X_EXIT = 5
        self.Y_EXIT = 11

    def solve_maze(self, maze, x_start, y_start):
        """This is the public method that will allow someone to use this class to solve the maze.
        Feel free to change the return type, or add more parameters if you like.
        But, it can be done exactly as it is here without adding anything other
        than code in the body."""

        # Holds current coordnates
        current_x = x_start
        current_y = y_start

        # Keeps method going until maze solved
        finish_bool = False

        while finish_bool == False:
            finish_bool = self._maze_traversal(maze, current_x, current_y)

        print("First maze is finished!")

    def _maze_traversal(self, maze, current_x, current_y):
        """This should be the recursive method that gets called to solve the maze.
        Feel free to have it return something if you would like. But, it can be
        done without having it return anything. Also feel free to change the
        signature to take in parameters that you might need.

        This is only a very small starting point.
        More than likely you will need to pass in at a minimum the current position
        in X and Y maze coordinates. EX: _maze_traversal(current_x, current_y)"""

        # Check current position to see if exit reached
        if current_x == self.X_EXIT and current_y == self.Y_EXIT:
            self.print_maze(maze)
            return True
        # Changes period to X if need be
        elif maze[current_x][current_y] == '.':
            maze[current_x][current_y] = 'X'
        # Check down
        elif maze[current_x + 1][current_y] == '.':
            self._maze_traversal(maze, current_x + 1, current_y)
        # Check up
        elif maze[current_x - 1][current_y] == '.':
            self._maze_traversal(maze, current_x - 1, current_y)
        # Check left
        elif maze[current_x][current_y-1] == '.':
            self._maze_traversal(maze, current_x, current_y - 1)
        # Check right
        elif maze[current_x][current_y + 1] == '.':
            self._maze_traversal(maze, current_x, current_y + 1)
        # Changes to O if at dead end
        else:
            maze[current_x][current_y] = 'O'
            self._maze_traversal(maze, current_x, current_y)

        self.print_maze(maze)

        return False
    
    def print_maze(self, maze):
        """Prints the maze for each step taken"""
        for y in maze:
            print()
            for symbols in y:
                print(symbols, end=" ")
