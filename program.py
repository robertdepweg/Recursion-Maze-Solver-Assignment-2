# Author: Robert Depweg
# Class: CIS226
# Date: 9/26/24
"""Program code"""

# First-party imports
from maze_solver import MazeSolver


def main(*args):
    """Method to run program"""
    # Starting Coordinates
    X_START = 1
    Y_START = 1

    # The first maze that needs to be solved.
    maze1 = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", ".", ".", ".", "#", ".", ".", ".", ".", ".", ".", "#"],
        ["#", ".", "#", ".", "#", ".", "#", "#", "#", "#", ".", "#"],
        ["#", "#", "#", ".", "#", ".", ".", ".", ".", "#", ".", "#"],
        ["#", ".", ".", ".", ".", "#", "#", "#", ".", "#", ".", "."],
        ["#", "#", "#", "#", ".", "#", ".", "#", ".", "#", ".", "#"],
        ["#", ".", ".", "#", ".", "#", ".", "#", ".", "#", ".", "#"],
        ["#", "#", ".", "#", ".", "#", ".", "#", ".", "#", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", "#"],
        ["#", "#", "#", "#", "#", "#", ".", "#", "#", "#", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ]

    # Create new instance of a MazeSolver
    maze_solver = MazeSolver()

    # Create the second maze by transposing the first maze
    maze2 = transpose_maze(maze1)

    # Solve the original maze
    maze_solver.solve_maze(maze1, X_START, Y_START)

    print("First maze is finished!")

    # Solve the transposed maze
    maze_solver.solve_maze(maze2, X_START, Y_START)

    print("Second maze is finished!")


def transpose_maze(maze_to_transpose):
    """Creates a transposed two dimensional list for the second maze from the first maze"""
    # The list that will be holding the transposed second maze
    new_maze = []

    for row_num in range(len(maze_to_transpose[0])):
        # New row to be placed in new_maze
        new_maze_row = []
        for item in maze_to_transpose:
            # Places each new item in corresponding maze row
            new_maze_row.append(item[row_num])
        # Adds new list to new maze
        new_maze.append(new_maze_row)
    return new_maze
