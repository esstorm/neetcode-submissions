class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        track = 0

        for num in nums:
            track ^= num

        return track
