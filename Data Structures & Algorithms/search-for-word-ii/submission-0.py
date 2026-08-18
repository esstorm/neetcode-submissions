from collections import defaultdict
from dataclasses import dataclass

class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = defaultdict(TrieNode)
        self.is_leaf: bool = False
        self.word = None

class Trie:
    def __init__(self, words: Optional[list[str]]):
        """Initialize trie"""
        self.root = TrieNode()

        if words is not None:
            for word in words:
                self.insert(word)

    def get_root(self) -> TrieNode:
        return self.root

    def insert(self, word: str) -> None:
        """Insert a word into the trie"""
        curr = self.root
        for letter in word:
            curr = curr.children[letter]
        curr.is_leaf = True
        curr.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])

        ans = []
        seen = set()
        trie = Trie(words)

        def dfs(x: int, y: int, node: Optional[Triechild]):
            if not (0 <= x < ROWS and 0 <= y < COLS):
                return

            if (x, y) in seen:
                return

            child = node.children.get(board[x][y])

            if child is None:
                return

            seen.add((x, y))

            if child.is_leaf:
                ans.append(child.word)
                child.is_leaf = False

            dfs(x-1, y, child)
            dfs(x+1, y, child)
            dfs(x, y-1, child)
            dfs(x, y+1, child)

            seen.remove((x, y))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.get_root())
        return ans
