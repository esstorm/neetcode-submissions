# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        queue = deque([root])

        while q:
            node = queue.popleft()

            if node is None:
                return None

            if max(p.val, q.val) < node.val:
                queue.append(node.left)
            elif min(p.val, q.val) > node.val:
                queue.append(node.right)
            else:
                return node
