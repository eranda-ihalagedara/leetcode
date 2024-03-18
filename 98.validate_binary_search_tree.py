class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.prev = -2**31-1

        def dfs(root):

            if root.left:
                if not dfs(root.left):
                    return False

            if self.prev >= root.val:
                return False
            self.prev = root.val
            if root.right:
                if not dfs(root.right):
                    return False
            return True
        
        return dfs(root)
		
		
    def isValidBST_optimized(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, pre, post):
            if not root: return True
            if pre >= root.val or root.val >= post: return False
            if not dfs(root.left, pre, root.val): return False
            return dfs(root.right, root.val, post)
        
        return dfs(root, -2**31-1, 2**31)