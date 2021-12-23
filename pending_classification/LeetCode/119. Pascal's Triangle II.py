class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[List[int]]
        """
        rowIndex += 1   # 注意和118提区别，这里第3行是118题里第4行

        if rowIndex == 0: return []
        if rowIndex == 1: return [1]

        lastLine = [1,1]       # 每次只保留最后一行的数据

        for i in range(2, rowIndex):   #notice the index, i = 2, when dealing line 3 

            curLine = []

            l = len(lastLine)   

            curLine.append(1)	# first 1
            # middle numbers
            for j in range(1, l):
            	curLine.append(lastLine[j-1] + lastLine[j])
            curLine.append(1)  # last 1

            lastLine = curLine

        return lastLine
        
if __name__ == '__main__':
	s = Solution()
	print(s.getRow(3))