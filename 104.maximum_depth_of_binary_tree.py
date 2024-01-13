# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0
            
        if root.left == None:
            ldepth = 0
        else:
            ldepth = self.maxDepth(root.left)
        
        if root.right == None:
            rdepth = 0
        else:
            rdepth = self.maxDepth(root.right)

        return max(ldepth, rdepth)+1