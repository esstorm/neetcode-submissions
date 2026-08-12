# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        q = deque([(root, 0)])
        ans = defaultdict(lambda: [])

        while q:
            node, lvl = q.popleft()
            ans[lvl].append(node.val)

            if node.left is not None:
                q.append((node.left, lvl + 1))

            if node.right is not None:
                q.append((node.right, lvl + 1))

        return [x[-1] for x in ans.values()]
