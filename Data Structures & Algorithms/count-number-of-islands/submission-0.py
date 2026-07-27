from collections import deque
from itertools import product

Grid = List[List[str]]

class Solution:
    def bfs(self, grid: Grid, visited: set[int, int], x1: int, y1: int):
        queue = deque([(x1, y1)])

        if grid[x1][y1] == "0":
            visited.add((x1, y1))
            return False

        while queue:
            node = queue.pop()
            (x2, y2) = node
        
            if node not in visited:  # TODO: remove unnecessary condition?
                visited.add(node)

                # neighbors = product(range(x2-1, x2+2), range(y2-1, y2+2))

                # for x3, y3 in neighbors:
                #     if  0 < x3 < len(grid) - 1 and 0 < y3 < len(grid[0]) - 1:
                #         if grid[x3][y3] == "1":
                #             queue.append((x3,y3))
                #         else:
                #             visited.add((x3, y3))

                if x2 < len(grid) - 1:
                    if grid[x2+1][y2] == "1":
                        queue.append((x2+1,y2))
                    else:
                        visited.add((x2+1, y2))
                if x2 > 0:
                    if grid[x2-1][y2] == "1":
                        queue.append((x2-1,y2))
                    else:
                        visited.add((x2-1, y2))
                if y2 < len(grid[0]) - 1:
                    if grid[x2][y2+1] == "1":
                        queue.append((x2, y2+1))
                    else:
                        visited.add((x2, y2+1))
                if y2 > 0:
                    if grid[x2][y2-1] == "1":
                        queue.append((x2, y2-1))
                    else:
                        visited.add((x2, y2-1))


        return True

    def numIslands(self, grid: Grid) -> int:
        visited = set()
        coords = product(range(len(grid)), range(len(grid[0])))
        count = 0

        for x, y in coords:
            if (x, y) in visited:
                continue

            if self.bfs(grid, visited, x, y):
                count += 1

        return count
        