# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        if not root:
            return None

        min_dif = float('inf')
        node_values = []
        node_queue = [root]

        while node_queue:
            node = node_queue.pop(0)
            
            for nv in node_values:
                min_dif = min(min_dif, abs(nv - node.val))
            node_values.append(node.val)

            if node.left:
                node_queue.append(node.left)
            
            if node.right:
                node_queue.append(node.right)

        return min_dif
	

    def getMinimumDifference_optimized(self, root: Optional[TreeNode]) -> int:

        ldif = float('inf')
        rdif = float('inf')
        if root.left:
            ldif = min(abs(root.val-root.left.val), self.getMinimumDifference(root.left))
        if root.right:
            rdif = min(abs(root.val-root.right.val), self.getMinimumDifference(root.right))
        
        return min(ldif, rdif)

    def getMinimumDifference_optimized2(self, root: Optional[TreeNode]) -> int:

        values = []
        node_stack = []
        node = root
        while node_stack or node:
            if node:
                node_stack.append(node)
                node = node.left
            else:
                node = node_stack.pop()
                values.append(node.val)
                node = node.right


        return min([values[i]-values[i-1] for i in range(1, len(values))])
	
	
    def getMinimumDifference_optimized3(self, root: Optional[TreeNode]) -> int:

        prev = -0x7FFFFFFF
        dif = 0x7FFFFFFF

        def min_dif(root):
            nonlocal prev, dif
            if root.left:
                min_dif(root.left)
            
            dif = min(dif, root.val-prev)
            prev = root.val
            if root.right:
                min_dif(root.right)

        min_dif(root)
        
        return dif

                





