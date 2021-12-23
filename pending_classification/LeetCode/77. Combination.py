class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.k = k
        self.n = n
        self.comb = []
        self.getComb([], 1)
        return self.comb

    def getComb(self, curComb, nextStart):
    	"""
    		curComb为当前获得的组合List
    		nextStart是当前数从range中可取的开始位置
    	"""
    	if len(curComb) == self.k:		# 如果当前组合长度等于k，保存
    		self.comb.append(curComb[:])	# 注意要复制保存[:]
    		
    	else:
    		for num in range(nextStart, self.n + 1):  # 
    			curComb.append(num)
    			self.getComb(curComb, num + 1)
    			curComb.pop()

if __name__ == "__main__":
	S = Solution()
	print(S.combine(5, 4))