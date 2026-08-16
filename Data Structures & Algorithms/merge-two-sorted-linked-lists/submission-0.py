# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        prev_ptr = None
        while list1 is not None or list2 is not None:
            curr_node = None
            if list1 is None:
                curr_node = list2
                list2 = list2.next
            elif list2 is None:
                curr_node = list1
                list1 = list1.next
            else:
                if list1.val <= list2.val:
                    curr_node = list1
                    list1 = list1.next
                else:
                    curr_node = list2
                    list2 = list2.next
            if prev_ptr is None:
                head = curr_node
            else:
                prev_ptr.next = curr_node
            prev_ptr = curr_node
        
        return head