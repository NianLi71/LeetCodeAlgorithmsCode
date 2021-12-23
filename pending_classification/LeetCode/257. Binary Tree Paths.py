# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        path = []
        if root:
        	self.findPath(root, [], path)

        path = ['->'.join(p) for p in path]

        return path

    def findPath(self, node, cur, path):
    	# leaf node
    	if not node.left and not node.right:
    		# cur.append(node.val)
    		path.append(cur[:] + [str(node.val)])
    		# cur.pop()
    		return

    	cur.append(str(node.val))	#这里将节点值存为str格式，方便最后统一的join操作
    	if node.left:
    		self.findPath(node.left, cur, path)
    	if node.right:
    		self.findPath(node.right, cur, path)
    	cur.pop()


if __name__ == '__main__':
	s = Solution()
	

	t1 = TreeNode(1)
	t2 = TreeNode(2)
	t3 = TreeNode(3)
	t5 = TreeNode(5)

	t1.left = t2
	t2.right = t5
	t1.right = t3

	print(s.binaryTreePaths(t1))