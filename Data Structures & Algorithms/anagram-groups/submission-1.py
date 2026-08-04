from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(lambda: [])

        for word in strs:
            groups[f"{sorted(word)}"].append(word)

        return list(groups.values())

