# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def stackReturn(self, root, s):
        
        if root.left == None and root.right == None:   
            s.append(root.val)         
            return s
        if root.left:
            self.stackReturn(root.left,s)
        if root.right:
            self.stackReturn(root.right,s)
        
        return s


    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        s = deque()
        s2 = deque()
        val1 = self.stackReturn(root1,s)
        val2 = self.stackReturn(root2, s2)
        if val1 == val2: 
            return True 
        else:
            return False 


     