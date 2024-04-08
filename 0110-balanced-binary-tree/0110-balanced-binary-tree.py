# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    final_answer = True 
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.dfs(root)
        return self.final_answer
    def dfs(self, root):
        if root == None: 
            return 0

        left_height = self.dfs(root.left) + 1 
        right_height = self.dfs(root.right) + 1 

        diff = abs(left_height - right_height)
        if diff > 1: 
            self.final_answer = False 

        return max(left_height, right_height)
        