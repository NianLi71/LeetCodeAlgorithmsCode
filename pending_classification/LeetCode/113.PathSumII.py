# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res_list = []

        def findPathSum(root: TreeNode, sum: int, cur_list: List[int]) -> None:
            if root is None:
                return
            cur_list.append(root.val)
            sum = sum-root.val
            if sum == 0 and root.left is None and root.right is None:  # reach leaf and sum is 0
                res_list.append(cur_list.copy())
            else:
                findPathSum(root.left, sum, cur_list)
                findPathSum(root.right, sum, cur_list)
            cur_list.pop()

        findPathSum(root, sum, [])

        return res_list



        
