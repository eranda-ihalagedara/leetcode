# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p==None and q==None:
            return True
        elif p==None or q==None:
            return False

        if p.val == q.val:
            node = True
        else:
            return False

        if p.left!=None and q.left!=None:
            ltree = self.isSameTree(p.left, q.left)
        elif p.left==None and q.left==None:
            ltree = True
        else:
            return False
        
        if p.right!=None and q.right!=None:
            rtree = self.isSameTree(p.right, q.right)
        elif p.right==None and q.right==None:
            rtree = True
        else:
            return False
        
        return node and ltree and rtree


    def isSameTree_optimized1(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p==None and q==None:
            return True
        elif p==None or q==None:
            return False

        node = p.val == q.val
        ltree = self.isSameTree(p.left, q.left)
        rtree = self.isSameTree(p.right, q.right)

