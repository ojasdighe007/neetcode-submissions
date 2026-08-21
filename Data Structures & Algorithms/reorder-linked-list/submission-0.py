# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mapPosToNode: dict[int, Optional[ListNode]] = {}
        curr = head
        idx = 0
        while curr is not None:
            mapPosToNode[idx] = curr
            curr = curr.next
            idx += 1

        length = idx
        turn = 0
        prevNode = None
        # print(length)
        # print(mapPosToNode)
        # print(mapPosToNode[length - math.ceil(3/2)])
        while turn < length:
            currNode = None
            if (turn%2) == 0:
                currNode = mapPosToNode[turn/2]
            else:
                currNode = mapPosToNode[length - math.ceil(turn/2)]
            if currNode != head:
                prevNode.next = currNode
            turn += 1
            prevNode = currNode
        if prevNode is not None:
            prevNode.next = None