class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums) - 1
        p = 0
        q = l
        
        while p <= q:
            i = p + ((q - p) // 2)
            val = nums[i]

            if val < target:
                p = i + 1
            elif val > target:
                q = i - 1
            else:
                return i
            
        return -1

