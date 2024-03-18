class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        if not root:
            return None
        stack = [root]
        inorder = []

        def dfs(root):
            
            if root.left:
                dfs(root.left)
            if len(inorder)==k:
                return
            inorder.append(root.val)
            if len(inorder)==k:
                return
            if root.right:
                dfs(root.right)
        dfs(root)
        return inorder[-1]
		

    def kthSmallest_alternative(self, root: Optional[TreeNode], k: int) -> int:
        
        if not root:
            return None
        stack = []
        cnode = root

        while cnode or stack:

            while cnode:
                stack.append(cnode)
                cnode = cnode.left
            
            cnode = stack.pop()
            k-=1
            if k == 0:
                return cnode.val
            cnode = cnode.right
        
        return inorder[-1]