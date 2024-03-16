# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        total_sum = 0
        node_stack = [root]

        while node_stack:
            cnode = node_stack.pop()

            if not cnode.left and not cnode.right:
                total_sum += cnode.val
            else:
                if cnode.right:
                    cnode.right.val += cnode.val*10
                    node_stack.append(cnode.right)

                if cnode.left: 
                    cnode.left.val += cnode.val*10
                    node_stack.append(cnode.left)

        return total_sum


    def sumNumbers_optimized(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        self.total_sum = 0
        
        def dfs(root):
            if not root.left and not root.right:
                self.total_sum += root.val
            else:
                if root.left:
                    root.left.val+= root.val*10
                    dfs(root.left)
                if root.right:
                    root.right.val+= root.val*10
                    dfs(root.right)
        dfs(root)
        return self.total_sum