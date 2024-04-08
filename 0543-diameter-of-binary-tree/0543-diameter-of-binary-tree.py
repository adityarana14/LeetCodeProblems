# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_answer = 0 
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None: 
            return 0 

        ans = self.dfs(root)
        return self.max_answer
    
    def dfs(self, root):
        if root == None: 
            return 0 

        left_len = self.dfs(root.left) + 1 
        right_len = self.dfs(root.right) + 1 
        
        sum_count = left_len + right_len - 2 
        if sum_count > self.max_answer: 
            self.max_answer = sum_count 

        return max(left_len, right_len)
    