class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pairs = {}

        for i, num in enumerate(numbers):
            if num in pairs:
                return ([pairs[num] + 1, i +1])
 
            pairs[target - num] = i