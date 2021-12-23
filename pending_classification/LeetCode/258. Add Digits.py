class Solution:
    def addOn(self, num, s):
    	if not num:
    		return s

    	cur = int(num[0]) + s
    	if cur >= 10:
    		cur = cur % 10 + int(cur / 10)
    	num.pop(0)
    	return self.addOn(num, cur)

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))
        return self.addOn(num, 0)
 
# N=(a[0] * 1 + a[1] * 10 + …a[n] * 10 ^n),and a[0]…a[n] are all between [0,9]

# we set M = a[0] + a[1] + …a[n]

# and another truth is that:

# 1 % 9 = 1

# 10 % 9 = 1

# 100 % 9 = 1

# so N % 9 = (a[0] * 1 + a[1] * 10 + …a[n] * 10 ^n) % 9
# 			= (a[0] + a[1] + …a[n]) % 9
# 所以 各个位置上数字和 % 9 = N % 9
# 去除0，9 的特殊情况

class S:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0: return 0
        if num % 9 == 0:
            return 9
        return num % 9    

if __name__ == '__main__':
	s = Solution()
	for i in range(5555, 6000):
		if i % 10 == 0:
			print('-'*20)
		print(i, s.addDigits(i), '-', i % 9)	


