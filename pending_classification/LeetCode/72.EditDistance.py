import numpy as np

def pt(dp, w1, w2):
    print(' '*7, end=' ')
    for e in w2:
        print('{}  '.format(e), end=' ')
    print()

    for i in range(dp.shape[0]):
        if i == 0:
            print(' ', end=' ')
        else:
            print(w1[i-1], end=' ')
        print(dp[i])

class Solution:
    def minDistanceWithPath(self, word1:str, word2:str) -> int:
        n = len(word1)
        m = len(word2)
        # dp = [ [0]*(len(word2)+1) for i in range(len(word1)+1) ]
        dp = np.zeros((n+1, m+1))
        # path = np.chararray(dp.shape)
        path = np.empty(dp.shape, dtype=object)
        path[:] = ' '

        # pt(path, word1, word2)
        # return 

        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j

        # print(dp)
        # pt(dp)

        for i in range(1,n+1):
            for j in range(1,m+1):
                # print(i, j, word1[:i], word2[:j])
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                    path[i][j] = 'e' 
                else:
                    choice_list = [dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1]
                    dir_list = ['u', 'l', 'd']
                    k = np.argmin(choice_list)
                    dp[i][j] = choice_list[k]
                    path[i][j] = dir_list[k]
        print(dp)
        pt(path, word1, word2)

    def minDistance(self, word1: str, word2: str) -> int:
        dp = [ [0]*(len(word2)+1) for i in range(len(word1)+1) ]
        # print(dp)
        n = len(word1)
        m = len(word2)

        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j

        # pt(dp)

        for i in range(1,n+1):
            for j in range(1,m+1):
                # print(i, j, word1[:i], word2[:j])
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1,
                                    dp[i][j-1]+1,
                                    dp[i-1][j-1]+1
                    )
        # pt(dp)

if __name__ == '__main__':
    s = Solution()
    word1 = "abcdef" 
    word2 = "abcgdef"
    # s.minDistance(word1, word2)
    s.minDistanceWithPath(word1, word2)
