# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == q and q is None:
            return True

        def dfs(p, q):
            x = p.val if p is not None else None
            y = q.val if q is not None else None
            if x != y:
                return False

            if p is not None or q is not None:
                x = p.left if p is not None else None
                y = q.left if q is not None else None
                if not dfs(x, y):
                    return False

            if p is not None or q is not None:
                x = p.right if p is not None else None
                y = q.right if q is not None else None
                if not dfs(x, y):
                    return False

            return True

        return dfs(p, q)


"""
None, None
"""