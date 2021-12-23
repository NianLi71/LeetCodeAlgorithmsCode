# 维护三个区间 [0, i), [i, j), [j, k) 分别代表0，1，2所在的区间
#
#
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        for k in range(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1
            print("[0,{0}), [{0}, {1}), [{1}, {2})".format(i, j, k))
            print(nums[:k+1])

nums = [2,1,2,2,2,1,1,0,2,0]
s = Solution()
s.sortColors(nums)

print(nums)