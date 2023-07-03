#!/usr/bin/python3

'''This module solves the N-queens puzzle'''

import sys


def initialize(n):
    '''
    Initialize a chessboard of size n x n

    Args:
        n (int): size of the chessboard

    Returns:
        A list of lists representing the chessboard
    '''
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return board


def cp_board(board):
    '''
    Copy a chessboard

    Args:
        board (list): The current working chessboard.

    Returns:
        A copy of the chessboard
    '''
    if isinstance(board, list):
        return list(map(cp_board, board))
    return board


def find_solution(board):
    '''
    Find a solution to the N-queens puzzle

    Args:
        board (list): The current working chessboard.

    Returns:
        A list of lists containing the coordinates of the queens
    '''
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def xout(board, row, col):
    '''
    X out all spots that are in the path of a queen

    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        col (int): The current working column.

    Returns:
        None
    '''
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def solve_recursively(board, row, queens, solutions):
    '''
    Solve the N-queens puzzle recursively

    Args:
        board (list): The current working chessboard.

    Returns:
        A list of lists containing the coordinates of the queens
    '''
    if queens == len(board):
        solutions.append(find_solution(board))
        return (solutions)
    for c in range(len(board)):
        if board[row][c] == " ":
            tmp = cp_board(board)
            tmp[row][c] = "Q"
            xout(tmp, row, c)
            solutions = solve_recursively(tmp, row + 1, queens + 1, solutions)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = initialize(int(sys.argv[1]))
    solutions = solve_recursively(board, 0, 0, [])
    for sol in solutions:
        print(sol)
