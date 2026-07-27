class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res = sorted([nums[i], nums[j], nums[k]])
                        if res not in result:
                            result.append(res)
        
        return result

