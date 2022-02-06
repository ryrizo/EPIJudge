import collections
import copy
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:
    '''Approach:
    Keep track of explored
    Check self
    Check each unexplored child
    '''
    explored = set()
    return search_maze_helper(maze, s, e, explored)

def search_maze_helper(maze, current, end, explored):
    if current == end:
        return [current]
    explored.add(current)
    for adjacent in path_adjacents(maze, current, explored):
        path_to_end = search_maze_helper(maze, adjacent, end, explored)
        if len(path_to_end) > 0:
            return [current] + path_to_end
    return []

def path_adjacents(maze, coord, explored):
    # Return white adjacents (no diagonals) - white is zero
    x, y = coord.x, coord.y
    candidates = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    adjacents = []
    for x, y in candidates:
        candidate = Coordinate(x, y)
        if in_bounds(maze, candidate) and \
            maze[x][y] == WHITE and \
            candidate not in explored:
            adjacents.append(candidate)
    return adjacents

def in_bounds(maze, coord):
    return 0 <= coord.x < len(maze) and 0 <= coord.y < len(maze[coord.x])

def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))
    # maze = [
    #     [1, 1, 1],
    #     [0, 0, 0],
    #     [1, 1, 1]
    # ]
    # coord = Coordinate(1, 1)
    # explored = set([coord])
    # print(path_adjacents(maze, coord, explored))
