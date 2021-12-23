# 经典动态规划问题，题目要求O(n)额外空间，从下往上递推，每次只保留最后层的计算结果

class Solution:
	def minimumTotal(self, triangle):
		"""
		:type triangle: List[List[int]]
		:rtype: int
		"""
		l = len(triangle)

		tempSumLine = triangle[-1]   
		for line in triangle[-2::-1]:   # 从倒数第二行开始递推计算
			for i in range(len(line)):
				pathSum = line[i] + (tempSumLine[i] if tempSumLine[i] < tempSumLine[i+1] 
													else tempSumLine[i+1])
				tempSumLine[i] = pathSum	# 节省空间，重复利用tempSumLine
			# print(tempSumLine)

		return tempSumLine[0]


if __name__ == '__main__':
	tri = [
	 [2],
	[3,4],
   [6,5,7],
  [4,1,8,3]
]
	# print(tri)
	s = Solution()
	print(s.minimumTotal(tri))