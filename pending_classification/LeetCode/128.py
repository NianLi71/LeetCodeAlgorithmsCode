'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

'''
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Runtime: 40 ms, faster than 91.85% of Python3 online submissions for Longest Consecutive Sequence.
        用set 实现O(n)
        '''
        if not nums:
            return 0

        s = set(nums)
        visit_set = set()
        total = 0
        for n in s:
            if n in visit_set:
                continue

            bigger = n+1
            while bigger in s:
                bigger+=1
                visit_set.add(bigger)

            little = n-1
            while little in s:
                little-=1
                visit_set.add(little)

            total = max(total, bigger - little -2 + 1)

        return total
    
if __name__ == '__main__':
    s = Solution()

    l = [1,4234,5324,123,2,3,4]
    print(s.longestConsecutive(l))