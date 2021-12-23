class Solution:
    def countPrimes(self, n):
        pass

#  解法一，太慢了，500000左右超时
class S_SLOW(Solution):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return 0
        if n == 3: return 1

        a = list(range(2, n))

        limit = n**0.5
        # print('limit', limit)
        i = 0
        while i < len(a) and a[i] < limit:
        	# print(a)
        	# print(i)
        	for k in a[i+1:]:    #从2开始，依次用筛法
        		if k % a[i] == 0:
        			a.remove(k)
        	i += 1
        return len(a)

#解法二，筛法，也不够快，1500000超时，经过优化，勉强AC，但效率排名后0.81%
class Solution2:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return 0
        if n == 3: return 1

        a = list(range(n))   # a = [0,1,2,3,...]

        a[1] = 0    # 去掉1
        l = n

        import math
        limit = math.sqrt(n)
  
        s = 2	# 每一次开始的位置索引，从a[2]开始，正好对应数字2
        while s < limit:

        	i = s
        	t = a[s]
        	# print(i, s)
        	while i + t < l:
        		a[i + t] = 0      # 以t为步长，依次划去数字
        		i += t

        	# 寻找下一起始数字
        	s += 1
        	while s < limit and a[s] == 0:
        		s += 1

        # print(a)

        p = 0
        for i in a:
        	if i:
        		p += 1
        return p



#解法三，看题解
#题解Hint3, O(N**1.5)的解法
import math
class S_N_1_5(Solution):
    def isPrime(self, k):
        if k <= 1: return False   # 0, 1不是素数
        l = math.sqrt(k) + 1
        for i in range(2, int(l)):
            if k % i == 0: return False
        return True

    def countPrimes(self, n):
        if n <= 2: return 0
        if n == 3: return 1

        count = 0
        for i in range(2, n):
            if self.isPrime(i):
                count += 1
        return count

#根据题解Hint6, 优化
class S_HINT_6(Solution):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return 0
        if n == 3: return 1

        a = list(range(n))   # a = [0,1,2,3,...]

        a[1] = 0    # 去掉1
        l = n

        import math
        limit = math.sqrt(n)
  
        s = 2   # 每一次开始的位置索引，从a[2]开始，正好对应数字2
        while s < limit:

            # i = s     #####优化这里
            i = s**2 - a[s]     ####然而并没有快多少，基本和Solution2一样
            t = a[s]
            # print(i, s)
            while i + t < l:
                a[i + t] = 0      # 以t为步长，依次划去数字
                i += t

            # 寻找下一起始数字
            s += 1
            while s < limit and a[s] == 0:
                s += 1

        # print(a)

        p = 0
        for i in a:
            if i:
                p += 1
        return p

#题解Hint8, 比我自己的Solution2快了一倍
class S_HINT_8(Solution):
    def countPrimes(self, n):
        if n <= 2: return 0
        if n == 3: return 1

        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False

        i = 2
        while i**2 < n:
            # print(i)
            if not isPrime[i]:
                i += 1
                continue
            j = i**2
            while j < n:
                isPrime[j] = False
                j += i

            i += 1
        
        # for k in range(len(isPrime)):
        #     if isPrime[k]:
        #         print(k, end = ' ')
        return sum(isPrime)

# 速度前82.93%，在HINT8基础上把for, while改为切片[::]提升很大，并用i*i代替i**0.5速度稍有提升
class SS(Solution):
    def countPrimes(self, n):
        if n <= 2: return 0

        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False

        l = int(n**0.5) + 1
        for i in range(2, l):
            if isPrime[i]:
                isPrime[i*i:n:i] = [False] * len(isPrime[i*i:n:i])
        # i = 2
        # while i**2 < n:
        #     # print(i)
        #     if not isPrime[i]:
        #         i += 1
        #         continue
        #     j = i**2
        #     while j < n:
        #         isPrime[j] = False
        #         j += i

        #     i += 1
        
        return sum(isPrime)


if __name__ == '__main__':
    # n = 1500000 时
    # s = S_N_1_5()     # 8.2s
    # s = S_HINT_6()    # 0.7s
    # s = Solution2()   # 0.7s
    # s = S_HINT_8()    # 0.4s
    s = SS()
    print(s.countPrimes(1500000))


    # s = S_SLOW()
    # print(s.countPrimes(50000))



