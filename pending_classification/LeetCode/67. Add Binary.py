class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a[::-1]		# 反转，将个位放到最左边对齐
        b = b[::-1]
        r = ''	#结果字符串
        ia = 0
        ib = 0
        c = 0	#进位标志
        while ia < len(a) or ib < len(b):

        	num_a = int(a[ia]) if ia < len(a) else 0
        	num_b = int(b[ib]) if ib < len(b) else 0
        	curRes = num_a + num_b + c

        	if curRes >= 2:
        		c = 1
        	else:
        		c = 0
        	r += str(curRes % 2)

        	ia += 1 
        	ib += 1

        if c == 1 :		# 加完后，还有进位
        	r += '1'
        return r[::-1]

if __name__ == '__main__':
	a = '111'
	b = '111'
	s = Solution()
	print(s.addBinary(a, b))