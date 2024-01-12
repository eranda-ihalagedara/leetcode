# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        ltree = [root.left]
        rtree = [root.right]

        while ltree and rtree:
            lnode = ltree.pop()
            rnode = rtree.pop()
            if lnode and rnode:
                if lnode.val != rnode.val:
                    return False
            elif lnode != rnode:
                return False
            if lnode:
                ltree.append(lnode.left)
                ltree.append(lnode.right)

            if rnode:
                rtree.append(rnode.right)
                rtree.append(rnode.left)
        
        if len(ltree)>0 or len(rtree)>0:
            return False

        return True
	
	def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        pairs = [[root.left, root.right]]

        while ltree and rtree:
            lnode = pairs[0]
            rnode = pairs[1]
			
            if lnode and rnode:
                if lnode.val != rnode.val:
                    return False
				pairs.append([lnode.left, rnode.right])
				pairs.append([lnode.right, rnode.left])
				
            elif lnode != rnode:
                return False

        return True
	
	def isSymmetric_recursion(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True

        return self.isMirrored(root.left, root.right)
		
		
	def isMirrored(self, lnode, rnode):
        if lnode == None and rnode == None:
            return True
        elif lnode == None or rnode == None:
            return False
        elif lnode.val != rnode.val:
            return False
        
        return self.isMirrored(lnode.left, rnode.right) and self.isMirrored(lnode.right, rnode.left)

    
