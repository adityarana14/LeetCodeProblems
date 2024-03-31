# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None 
        behind = head 
        curr = head 
        forward = None 
        count = 0 

        while count != n-1: 
            curr = curr.next 
            forward = curr
            count = count + 1 

        while curr.next is not None:
            prev = behind
            behind = behind.next 
            curr = curr.next 


        if prev != None:
            prev.next = prev.next.next
        else: 
            if behind.next != None:
                head = behind.next    
            else: return None 
        
        return head 