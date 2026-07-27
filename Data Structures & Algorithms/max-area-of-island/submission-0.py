Grid = List[List[int]]

class Solution:
    def maxAreaOfIsland(self, grid: Grid) -> int:
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(grid: Grid, i: int, j: int) -> int:
            stack = [(i, j)]
            count = 0

            while stack:
                i, j = stack.pop()

                if grid[i][j] == 1:
                    count += 1
                    grid[i][j] = 0

                    for dx, dy in neighbors:
                        x = i + dx
                        y = j + dy
    
                        if not 0 <= x < len(grid):
                            continue
    
                        if not 0 <= y < len(grid[0]):
                            continue
    
                        if grid[x][y] == 1:
                            stack.append((x, y))

            return count




        max_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_count = max(dfs(grid, i, j), max_count)

        return max_count
