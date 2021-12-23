# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	# def levelOrder(self, root):
	# 	"""
	# 	:type root: TreeNode
	# 	:rtype: List[List[int]]
	# 	"""
	# 	res = []
	# 	if root:
	# 		cur = [root]
	# 		res = [[root.val]]
	# 		while cur:
	# 			nextLevel = []
	# 			res.append([])
	# 			for node in cur:
	# 				if node.left:
	# 					nextLevel.append(node.left)
	# 					res[-1].append(node.left.val)
	# 				if node.right:
	# 					nextLevel.append(node.right)
	# 					res[-1].append(node.right.val)
	# 			cur = nextLevel

	# 		res.pop()	#最后一层时，res会提前加入一个[]，最后Pop掉就好

	# 	return res

	# version 2 结构上做了点小修
	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		res = []
		if root:
			cur = [root]
			while cur:
				nextLevel = []
				res.append([])
				for node in cur:
					res[-1].append(node.val)
					if node.left:
						nextLevel.append(node.left)
					if node.right:
						nextLevel.append(node.right)
				cur = nextLevel

		return res

# 看题解，看到一个很精妙的解法，相当于把写的while，for都换成列表推导了
#
#def levelOrder(self, root):
    # ans, level = [], [root]
    # while root and level:
    #     ans.append([node.val for node in level])            
    #     level = [kid for n in level for kid in (n.left, n.right) if kid]
    # return ans

if __name__ == '__main__':
	s = Solution()
	
	t1 = TreeNode(1)
	t2 = TreeNode(2)
	t3 = TreeNode(3)
	t4 = TreeNode(4)
	t5 = TreeNode(5)
	t6 = TreeNode(6)
	t7 = TreeNode(7)

	t1.left = t2
	t1.right = t3

	t2.left = t4
	t2.right = t5

	t3.left = t6
	t3.right = t7

	print(s.levelOrder(t1))