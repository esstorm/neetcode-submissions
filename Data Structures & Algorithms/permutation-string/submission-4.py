from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        count = Counter(s1)

        for l in range(len(s2) - len(s1) + 1):
            if not any(count.values()):
                return True

            count2 = Counter(s2[l:l+n])
            print(f"{count=} {count2=}")
            if count2 == count:
                return True

        return False
