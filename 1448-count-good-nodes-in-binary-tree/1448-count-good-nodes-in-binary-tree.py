# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countGoodNodes(self, root, bestNode,  a):
        
        if root == None: 
            return a 

        if root.val >= bestNode:
            bestNode = root.val 
            a.append(bestNode)

        if root.left:
            val1 = self.countGoodNodes(root.left, bestNode, a)
            
            
        if root.right: 
            val2 = self.countGoodNodes(root.right, bestNode, a)
            

        return a 




    def goodNodes(self, root: TreeNode) -> int:
        bestNode = root.val
        return len(self.countGoodNodes(root, bestNode,[]))



        