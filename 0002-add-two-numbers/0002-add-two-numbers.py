# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # head1 = l1 
        # head2 = l2
        # print(head1)
        # carry = 0 
        # count = 0 
        # while l1 != None: 
        #     count = count + 1 
        #     l1 = l1.next
        
        # count2 = 0 
        # while l2 != None: 
        #     count2 = count2 + 1 
        #     l2 = l2.next 

        # print(count)
        # print(count2)

        # if count > count2 : 
        #     dummy_linkedlist = head1 
        # else: 
        #     dummy_linkedlist = head2

        # head3 = dummy_linkedlist
        # print(head3)

        # while head1 != None or head2 != None:
        #     print("printing")
        #     sum = 0 
        #     if head1 != None and head2 != None:
        #         val1 = head1.val 
        #         val2 = head2.val
        #         sum = val1 + val2 + carry 

        #         if sum > 9:
        #             carry = 1 
        #         else: 
        #             carry = 0 
                
        #         sum = sum % 10
        #         head3.val = sum 
        #         head3 = head3.next

        #         head1 = head1.next
        #         head2 = head2.next

        #     elif head1 != None and head2 == None: 
        #         if carry == 0: 
        #             sum = head1.val
        #             head3.val = sum; 
        #             head3 = head3.next
    
        #         else: 
        #             sum = head1.val + carry
        #             if sum > 9: 
        #                 sum = sum % 10 
        #                 carry = 1  
        #             else: 
        #                 carry = 0 
        #             head3.val = sum
        #             head3 = head3.next

        #         head1 = head1.next
    
        #     else: 
        #         if carry == 0: 
        #             sum = head2.val
        #             head3.val = sum; 
        #             head3 = head3.next
    
        #         else: 
        #             sum = head2.val + carry 
        #             if sum > 9:
        #                 sum = sum % 10 
        #                 carry = 1 
        #             else: 
        #                 carry = 0
        #             head3.val = sum
        #             head3 = head3.next

        #         head2 = head2.next
        # head4 = dummy_linkedlist
        # while head4.next != None:
        #     head4 = head4.next
        # if carry != 0:
        #     new_node = ListNode(1)
        #     head4.next = new_node
            


        # return dummy_linkedlist

        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result
        

        
        