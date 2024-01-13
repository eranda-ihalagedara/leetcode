# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False
        
        def check_sum(node, tval):

            if node.left == None and node.right == None:
                if node.val == tval:
                    return True
                else:
                    return False
            
            lpath, rpath = False, False

            if node.left != None:
                lpath = check_sum(node.left, tval - node.val)

            if node.right != None:
                rpath = check_sum(node.right, tval - node.val)
            
            return lpath or rpath
        
        return check_sum(root, targetSum)
		
		

	def hasPathSum_optimized(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
		if root.left == None and root.right == None:
			if root.val == targetSum:
				return True
			else:
				return False
        
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

	# DFS with stack
	def hasPathSum_dfs(self, root, targetSum):
		if not root:
			return False
		stack = [(root, root.val)]
		while stack:
			curr, val = stack.pop()
			if not curr.left and not curr.right and val == targetSum:
				return True
			if curr.right:
				stack.append((curr.right, val+curr.right.val))
			if curr.left:
				stack.append((curr.left, val+curr.left.val))
		return False
		
	# BFS with queue
	def hasPathSum_dfs(self, root, targetSum):
		if not root:
			return False
		queue = [(root, root.val)]
		while stack:
			curr, val = stack.pop(0)
			if not curr.left and not curr.right and val == targetSum:
				return True
			if curr.right:
				stack.append((curr.right, val+curr.right.val))
			if curr.left:
				stack.append((curr.left, val+curr.left.val))
		return False