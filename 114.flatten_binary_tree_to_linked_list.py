# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cnode = head = TreeNode(0)

        node_stack = [root]

        while node_stack:
            node = node_stack.pop()
            if node:
                node_stack.append(node.right)
                node_stack.append(node.left)
                node.left = None
                cnode.right = node
                cnode = cnode.right
        
        return head.right


    def flatten_optimizedI(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        self.flatten(root.left)
        self.flatten(root.right)

        right_subtree = root.right
        root.right = root.left
        root.left = None

        cnode = root
        while cnode.right:
            cnode = cnode.right
        
        cnode.right = right_subtree

        return root
		

    def flatten_optimizedII(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        cnode = root
        while cnode:

            if cnode.left:
                lnode = cnode.left
                while lnode.right:
                    lnode = lnode.right
                lnode.right = cnode.right

                cnode.right = cnode.left
                cnode.left = None

            cnode = cnode.right
        
        return root
            