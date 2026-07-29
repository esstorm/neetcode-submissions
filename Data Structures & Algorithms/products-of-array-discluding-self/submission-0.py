class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def get_prod(s: List[int]):
            ans = 1
            for num in s:
                ans *= num

            return ans

        n = len(nums)
        return [get_prod(nums[0:i] + nums[i+1:n]) for i in range(n)]
