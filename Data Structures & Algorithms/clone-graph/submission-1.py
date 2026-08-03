"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        q = deque([node])
        seen = {node: Node(node.val)}

        while q:
            cur = q.popleft()
            for n in cur.neighbors:
                if n not in seen:
                    seen[n] = Node(n.val)
                    q.append(n)
                seen[cur].neighbors.append(seen[n])
        
        return seen[node]
        