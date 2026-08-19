class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        dirs = (
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        )

        skip = {}
        fresh = {}
        rotten = {}

        for r in range(ROWS):
            for c in range(COLS):
                val = grid[r][c]

                if val == 1:
                    fresh[(r, c)] = 1
                elif val == 2:
                    rotten[(r, c)] = 1

        count = 0
        while fresh:
            new = {}
            for r, c in rotten:
                for _r, _c in dirs:  # TODO: optimize when no longer need to infect nearby fruit
                    x, y = r + _r, c + _c
                    if not (0 <= x < ROWS and 0 <= y < COLS):
                        continue

                    val = grid[x][y]
                    if val == 1:
                        if (x, y) in fresh:
                            fresh.pop((x, y))
                            new[(x, y)] = 1
                            
            if not new:
                break

            count += 1
            rotten = new

        if fresh:
            return -1
                    
        return count
    
    
    