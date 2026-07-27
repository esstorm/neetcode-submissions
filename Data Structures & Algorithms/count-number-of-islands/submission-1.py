from typing import List

Grid = List[List[str]]

NEIGHBOR_OFFSETS = ((1, 0), (-1, 0), (0, 1), (0, -1))


class Solution:
    def sink(self, grid: Grid, x1: int, y1: int) -> None:
        """Flood-fill the island containing (x1, y1), marking it visited."""
        rows, cols = len(grid), len(grid[0])
        stack = [(x1, y1)]
        grid[x1][y1] = "0"  # mark visited immediately, not on pop

        while stack:
            x2, y2 = stack.pop()
            for dx, dy in NEIGHBOR_OFFSETS:
                nx, ny = x2 + dx, y2 + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
                    grid[nx][ny] = "0"  # mark before pushing, not after popping
                    stack.append((nx, ny))

    def numIslands(self, grid: Grid) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1":
                    count += 1
                    self.sink(grid, x, y)

        return count