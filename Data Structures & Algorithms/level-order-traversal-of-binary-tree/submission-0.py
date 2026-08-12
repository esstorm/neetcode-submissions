# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q = deque([(root, 0)])
        ans = defaultdict(lambda: [])

        while q:
            node, lvl = q.popleft()

            ans[lvl].append(node.val)

            if node.left is not None:
                q.append((node.left, lvl+1))
            if node.right is not None:
                q.append((node.right, lvl+1))

        return list(ans.values())


"""
TCs:
q = [(1, 0), (2, 1), (3, 1), (4, 2), (5, 2), (6, 2), (7, 2)]
ans = {
    0: [1],
    1: [2, 3],
    2: [4, 5, 6, 7],
    ...
}

node, lvl = 1, 0
"""
