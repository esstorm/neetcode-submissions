class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1

        count = Counter()
        l = 0
        ans = 0

        for r in range(len(s)):
            count[s[r]] += 1

            most_common = count.most_common(1)[0][1]
            while sum(count.values()) - most_common > k:
                count[s[l]] -= 1
                l += 1

            ans = max(sum(count.values()), ans)

        return ans

"""
TCs:
1. s = "XYX"
count = {
"X": 1,
}

2. s = "XX"


3. s = ""


4. s = "AAABCC"

"""
