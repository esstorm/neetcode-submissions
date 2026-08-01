class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (l := len(s)) < 2:
            return l

        c = l = 0
        seen = {}

        for r in range(len(s)):
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1

            seen[s[r]] = r
            c = max(c, r - l + 1)

        return c
