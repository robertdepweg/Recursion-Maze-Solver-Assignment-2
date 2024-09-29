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

    # Solve the transposed maze
    maze_solver.solve_maze(maze2, X_START, Y_START)


def transpose_maze(maze_to_transpose):
    """This method will take in a 2d list (list of lists) and return a new
    2d list maze that is flipped along the diagonal, or in mathematical terms,
    transposed.

    ie. If the array looks like:
    1, 2, 3
    4, 5, 6
    7, 8, 9
    Then the returned result will be:
    1, 4, 7
    2, 5, 8
    3, 6, 9

    It is important that you make a new 2d list and copy each element from the
    original to the new transposed one. Failure to do so may lead you to only
    be able to solve the transposed one.
    """
    new_maze = [
    [], [], [], [], [], [], [], [], [], [], [], []
    ]
    for maze_x_coordnate, list_of_list_num in enumerate(maze_to_transpose):
        for maze_y_coordnate, value in enumerate(list_of_list_num):
            if maze_x_coordnate == maze_y_coordnate:
                new_maze[maze_x_coordnate][maze_y_coordnate] = value
            else:
                new_maze[(len(list_of_list_num) - 1) - maze_x_coordnate][(len(maze_to_transpose) - 1) - maze_y_coordnate] = value
    return new_maze
