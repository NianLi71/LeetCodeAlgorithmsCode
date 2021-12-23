class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        '''
        Runtime: 96 ms, faster than 84.34% of Python3 online submissions for Distinct Subsequences.

        在算法2的基础上，不用numpy
        复杂度O(n^3)
        
        还有dp优化的余地
        '''
        if not s or not t:
            return 0

        c_list = []
        f = []
        for tc in t:
            cur_list = []
            ff = []
            for i, sc in enumerate(s):
                if tc == sc:
                    cur_list.append(i)
                    ff.append(0)
            c_list.append(cur_list)
            f.append(ff)
        
        # print(c_list)

        for i in range(len(f[-1])):
            f[-1][i]=1
        # print(f)

        def get_bigger_index_list(list_1, num):
            for i, e in enumerate(list_1):
                if e > num:
                    yield i
     
        for i in range(len(c_list)-2, -1, -1):  # 从下往上枚举每一行
            j = i + 1
            for k in range(len(c_list[i])): #对每一行中每个元素
                for h in get_bigger_index_list(c_list[j], c_list[i][k]):
                    # print(h, end=' ')
                    f[i][k] += f[j][h]
                # print()

        return sum(f[0])


class Solution2:
    def numDistinct(self, s: str, t: str) -> int:
        '''
        using numpy, leetcode does not support numpy
        '''
        if not s or not t:
            return 0

        import numpy as np
        c_list = []
        f = []
        for tc in t:
            cur_list = []
            ff = []
            for i, sc in enumerate(s):
                if tc == sc:
                    cur_list.append(i)
                    ff.append(0)
            c_list.append(np.array(cur_list))
            f.append(ff)
        
        # print(c_list)
        # print(type(c_list[0]))
        # print( c_list[0][c_list[0] > 2])
        # print( np.nonzero(c_list[0] > 2))

        for i in range(len(f[-1])):
            f[-1][i]=1
        # print(f)
     
        for i in range(len(c_list)-2, -1, -1):
            j = i + 1
            for k in range(len(c_list[i])):
                # print(np.nonzero(c_list[j] > c_list[i][k])[0])
                for h in np.nonzero(c_list[j] > c_list[i][k])[0]:
                # for h in c_list[j][c_list[j] > k]:
                    # print(h, end=' ')
                    f[i][k] += f[j][h]
                # print()

        return sum(f[0])
    

class Solution1:
    def numDistinct(self, s: str, t: str) -> int:
        '''
        超时
        递归解法，构造串判断
        '''
        total = 0
        def _form_string(cur_str, i, s, t):
            if cur_str == t:
                nonlocal total
                total += 1
                # print('*',cur_str, ll)
                return
            if len(cur_str) == len(t):  # same len but not match
                return

            for j in range(i, len(s)):
                # print(cur_str, s[j], j, i)
                next_str = cur_str+s[j]
                # ll.append(j)
                if t.startswith(next_str):
                    _form_string(next_str, j+1, s, t)
                # ll.pop()

        _form_string('', 0, s, t)

        # print(total)

        return total
    
if __name__ == '__main__':
    s = Solution()

    # S = "rabbbit"
    # T = "rabbit"

    # S = "babgbag"
    # T = "bag"

    # S = ""
    # T = ""

    S="aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
    T="bddabdcae"

    print(s.numDistinct(S, T))