# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return True 

        return self.check_isValid_BST(root, float("-inf"), float("inf"))

    def check_isValid_BST(self, root, left, right):
        if not root: 
            return True 

        if not (root.val > left and root.val < right):
            return False 

        return ((self.check_isValid_BST(root.left,  left, root.val) and 
        self.check_isValid_BST(root.right, root.val, right)))
