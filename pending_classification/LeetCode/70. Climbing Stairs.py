class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 可以用递归做，这里用递推实现
        if n == 1: return 1
        if n == 2: return 2
        f_1 = 2 	# 距离当前1个距离的跳法数
        f_2 = 1	 	# 距离当前2个距离的跳法数

        f_n = f_2
        for i in range(3, n + 1):	# 我们从3开始跳
        	f_n = f_2 + f_1
        	f_2 = f_1
        	f_1 = f_n
        return f_n

if __name__ == '__main__':
	s = Solution()
	print(s.climbStairs(3))
