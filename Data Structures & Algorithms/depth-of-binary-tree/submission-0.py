# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node: TreeNode):
            stack = [(node, 1)]
            visited = set()
            max_depth = 0

            while stack:
                n, c = stack.pop()
                
                if n is None:
                    break

                max_depth = max(c, max_depth)
                visited.add(n)

                if n.right is not None:
                    if n.right not in visited:
                        stack.append((n.right, c+1))

                if n.left is not None:
                    if n.left not in visited:
                        stack.append((n.left, c+1))

            return max_depth

        return dfs(root)
        