class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0

        chars = set()

        l = r = 0
        max_s = 0

        while r < len(s):
            if s[r] not in chars:
                chars.add(s[r])
                max_s = max(max_s, len(chars))
                r += 1
            else:
                chars.remove(s[l])
                l += 1

        return max_s
            