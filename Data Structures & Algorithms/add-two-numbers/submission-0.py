# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3: Optional[ListNode] = None
        carry: int = 0
        prevNode: Optional[ListNode] = None
        while l1 is not None or l2 is not None:
            val1 = val2 = 0
            if l1 is not None:
                val1 = l1.val
                l1 = l1.next
            if l2 is not None:
                val2 = l2.val
                l2 = l2.next
            
            currSum = int((val1 + val2 + carry))%10
            carry = int((val1 + val2 + carry))/10

            sumNode = ListNode(currSum)
            if prevNode is None:
                l3 = sumNode
            else:
                prevNode.next = sumNode
            prevNode = sumNode
            
        
        if int(carry):
            sumNode = ListNode(int(carry))
            prevNode.next = sumNode
        
        return l3

        
