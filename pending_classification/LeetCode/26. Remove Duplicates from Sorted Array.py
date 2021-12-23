# class Solution:
# 	def removeDuplicates(self, nums):
# 		"""
# 		:type nums: List[int]
# 		:rtype: int
# 		"""
# 		l = 0
# 		i = 0
# 		while i < len(nums):
# 			l += 1

# 			j = i + 1
# 			while j < len(nums) and nums[j] == nums[i]:   # 这里nums的长度在变，j位置不变
# 				nums.pop(j)
# 			i = j

# 		return l

# 不用pop, 稍微快一些
class Solution:
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums: return 0

		j = 1
		i = 0
		for i in range(1, len(nums)):
			if nums[i] != nums[i-1]:
				nums[j] = nums[i]
				j += 1

		return j

if __name__ == '__main__':
	s = Solution()
	nums = [1,2,3]
	print(s.removeDuplicates(nums))
	print(nums)