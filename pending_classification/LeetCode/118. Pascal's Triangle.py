class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: return []
        if numRows == 1: return [[1]]

        tri = [[1],[1,1]]

        for i in range(2, numRows):   #notice the index, i = 2, when dealing line 3 

        	curLine = []
        	lastLine = tri[i-1]

        	l = len(lastLine)

        	curLine.append(1)	# first 1
        	# middle numbers
        	for j in range(1, l):
        		curLine.append(lastLine[j-1] + lastLine[j])
        	curLine.append(1)  # last 1
        	tri.append(curLine)	

        return tri
        
if __name__ == '__main__':
	s = Solution()
	print(s.generate(5))