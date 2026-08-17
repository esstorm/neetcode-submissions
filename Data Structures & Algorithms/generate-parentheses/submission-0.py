class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stack = []

        def backtrack(curr, remain):
            if remain == 0:
                if not stack:
                    ans.append("".join(curr[:]))
                return

            # Choice 1: place "("
            curr.append("(")
            stack.append("(")
            backtrack(curr, remain - 1)
            stack.pop()
            curr.pop()

            # Choice 2: place ")" — only if there's an unmatched "(" to close
            if stack:
                curr.append(")")
                stack.pop()
                backtrack(curr, remain - 1)
                stack.append("(")   # restore the "(" we just closed
                curr.pop()

        backtrack([], 2 * n)
        return ans