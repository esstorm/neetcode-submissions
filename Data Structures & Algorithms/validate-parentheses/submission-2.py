class Solution:
    def get_pair(self, c: str):
        pairs = {
            "(": ")",
            "{": ")",
            "[": "]",
            ")": "(",
            "}": "{",
            "]": "[",
        }
        try:
            return pairs[c]
        except KeyError:
            raise Exception(f"No pair for {c}")

    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in ("(", "{", "["):
                stack.append(c)
            elif not len(stack) or self.get_pair(c) != stack.pop():
                return False

        return len(stack) == 0