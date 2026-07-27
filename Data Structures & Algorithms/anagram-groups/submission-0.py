from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(lambda: [])

        for s in strs:
            key = "".join(sorted(s))
            res[key].append(s)

        return res.values()

            
