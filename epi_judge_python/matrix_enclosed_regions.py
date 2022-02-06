from typing import List
from collections import deque

from test_framework import generic_test


def fill_surrounded_regions(board: List[List[str]]) -> None:
    '''Approach
    0) Create all B result matrix
    1) Enqueue boundary whites
    2) BFS setting spaces in 0 to saved
    '''
    rows = len(board)
    cols = len(board[0])
    q = deque()
    enqueue_boundary_w(board, q)
    while q:
        x, y = q.popleft()
        board[x][y] = 'T'
        enqueue_adjacents(board, x, y, q)
    board[:] = [['B' if c != 'T' else 'W' for c in row] for row in board]

def enqueue_adjacents(board, x, y, q):
    for row, col in ((x+1, y), (x-1, y), (x, y-1), (x, y+1)):
        # In range and a W
        if 0 <= row < len(board) and 0 <= col < len(board[row]) and \
            board[row][col] == 'W':
            q.append((row, col))

def enqueue_boundary_w(board, q): 
    # Return a list of boundary tuples 
    for i, row in enumerate(board):
        if i == 0 or i == len(board) - 1: # First or last row
            for col, value in enumerate(row):
                if value == 'W':
                    q.append((i, col))
        else:
            if row[0] == 'W':
                q.append((i, 0))
            if row[-1] == 'W':
                q.append((i, len(row) - 1))

def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
