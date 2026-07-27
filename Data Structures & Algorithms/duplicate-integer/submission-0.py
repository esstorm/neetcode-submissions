from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(lambda: 0)

        for num in nums:
            count[num] += 1
            if count[num] > 1:
                return True
            
        return False

            
         