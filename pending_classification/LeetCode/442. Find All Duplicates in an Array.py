# -*- coding:utf8 -*-

# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array),
# some elements appear [twice] and others appear [once].

# Find all the elements that appear twice in this array.

# Could you do it without extra space and in O(n) runtime?

# Example:
# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [2,3]

# 题解：
# 这道题有很多细节，每个元素a[i]：1 ≤ a[i] ≤ n, n是数组大小
# 元素只会出现2次或1次
# O(n)时间复杂度，无额外空间

# 利用奇偶性，因为每个元素值 1 ≤ a[i] ≤ n， 那么 0 ≤ a[i] -1 ≤ n - 1，
# 正好能对应成数组索引，如果a[i]出现两次，那么a[i]-1也出现两次。利用正负号奇偶性，
# 	1.对a中每个元素，从左到右扫描，判断 a[ abs(a[i]） - 1 ] 的符号，若<0，则说明之前出现过a[i],
#	 将a[i] 保存至输出列表
# 	（之所以用abs，是因为a[i]可能因为左边的数影响符号变为负号）
# 	2.若a[ abs(a[i]） - 1 ] 符号 > 0，则是第一次出现a[i], 将a[ abs(a[i]） - 1 ] 符号置为负号

class Solution:
	def findDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		l = []
		for k in nums:
			if nums[abs(k) - 1] < 0:
				l.append(abs(k))
			else:
				nums[ abs(k) - 1] *= -1
				
		return l

if __name__ == '__main__':
	s = Solution()
	l = [4,3,2,7,8,2,3,1]
	print(s.findDuplicates(l))
        