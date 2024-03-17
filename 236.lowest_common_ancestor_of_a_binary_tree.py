class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root or root in {p,q}: return root

        left = self.lowestCommonAncestor(root.left, p,q)
        right = self.lowestCommonAncestor(root.right, p,q)

        if left and right: return root
        return left or right