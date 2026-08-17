class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        chars = set(word)
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(x: int, y: int, i: int):
            if i == len(word):
                return True

            if not (0 <= x < ROWS) or not (0 <= y < COLS):
                return False

            if (x, y) in seen or word[i] != board[x][y]:
                return False

            seen.add((x, y))
            found = (
                dfs(x+1, y, i+1)
                or dfs(x-1, y, i+1)
                or dfs(x, y+1, i+1)
                or dfs(x, y-1, i+1)
            )
            seen.remove((x, y))
            return found


        for x in range(ROWS):
            for y in range(COLS):
                if board[x][y] not in chars:
                    board[x][y] = None
                    continue
                if dfs(x, y, 0):
                    return True

        return False