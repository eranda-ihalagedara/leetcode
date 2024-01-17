# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return None
            
        mid = len(nums)//2

        root = TreeNode(nums[mid])

        if mid > 0:
            root.left  = self.sortedArrayToBST(nums[:mid])

        if mid < len(nums):
            root.right = self.sortedArrayToBST(nums[mid+1:])

        return root
	
    def sortedArrayToBST_optimized(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return None

        mid = len(nums)//2

        return TreeNode(nums[mid],
        self.sortedArrayToBST(nums[:mid]),
        self.sortedArrayToBST(nums[mid+1:])
        )