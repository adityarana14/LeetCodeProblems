# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Lot of redundancy is there in the code, specially we are returning the value which is not necessary. It is there because I was checking the self functionality. 
        self.answer = None 

        def searchNumber(root, val):
            if not root: 
                return None
            if root.val == val:
                self.answer = root
                return root 
            elif root.val > val:
                return searchNumber( root.left, val)
            else : 
                return searchNumber( root.right,  val)
            
        final_answer = searchNumber( root, val)
        
        return self.answer

        
     