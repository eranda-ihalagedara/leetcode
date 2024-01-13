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