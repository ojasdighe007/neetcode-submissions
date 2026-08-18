# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def calcSizeOfList(self, head: Optional[ListNode]) -> int:
        curr_ptr = head
        sz = 0
        while curr_ptr is not None:
            sz += 1
            curr_ptr = curr_ptr.next
        return sz

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = self.calcSizeOfList(head)
        prev_ptr = None
        curr_ptr = head
        for i in range(1,sz+1):
            if i == sz-n+1:
                if prev_ptr is not None:
                    prev_ptr.next = curr_ptr.next
                else:
                    head = head.next
            prev_ptr = curr_ptr
            curr_ptr = curr_ptr.next
        return head


