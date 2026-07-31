class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		if not nums:
			return 0
		
		nums = sorted(nums)
		count = ans = 1
		
		for i in range(1, len(nums)):
			if nums[i-1] == nums[i] - 1:
				count +=1
				ans = max(count, ans)
			elif nums[i-1] == nums[i]:
				continue
			else:
				count = 1
		
		return ans