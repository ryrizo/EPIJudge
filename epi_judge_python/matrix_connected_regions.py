from typing import List
from collections import deque

from test_framework import generic_test


def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    '''Approach:
    BFS flipping the colors
    Enqueue adjacents of the target color
    On dequeue, flip color of self. 
    '''
    color_to_flip = image[x][y]
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        image[x][y] = not color_to_flip
        enqueue_adjacents(x, y, color_to_flip, image, q)

def enqueue_adjacents(x, y, color_to_flip, image, q):
    # Return in range, adjacents of target color
    candidates = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    for row, col in candidates:
        if 0 <= row < len(image) and 0 <= col < len(image[row]) and \
            image[row][col] == color_to_flip:
            q.append((row, col))

def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
