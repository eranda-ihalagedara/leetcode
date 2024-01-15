# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ncount = 0

        node_stack = [root]

        while node_stack:
            node = node_stack.pop()
            ncount+=1

            if node.left:
                node_stack.append(node.left)

            if node.right:
                node_stack.append(node.right)

        return ncount

    def countNodes_oneline(self, root: Optional[TreeNode]) -> int:
		# counting 1 for every node that is not None
        return 1 + self.countNodes(root.left) + self.countNodes(root.right) if root else 0
		

    def countNodes_optimized1(self, root):

        if not root : return 0
        
		l,r =1,1
		
        left = right = root                           # compute both left and right heights of
        while left  := left.left   : l += 1           # each subtree by going all way down to
        while right := right.right : r += 1           # the left and right (in logN time)

        if l == r : return 2**l - 1                   # if it's a full tree, its size is known
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)