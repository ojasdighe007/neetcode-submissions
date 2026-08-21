# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rec(self,root: Optional[ListNode], curr: Optional[ListNode]) -> Optional[ListNode]:
        if curr is None:
            return root
        
        root = self.rec(root, curr.next)
        if root is None:
            return None

        tmp = None
        if root == curr or root.next == curr:
            curr.next = None
        else:
            tmp = root.next
            root.next = curr
            curr.next = tmp
        return tmp

    def reorderList(self, head: Optional[ListNode]) -> None:
        head = self.rec(head, head.next)