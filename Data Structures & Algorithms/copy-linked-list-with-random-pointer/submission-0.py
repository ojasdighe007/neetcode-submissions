"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeToPosMapOrigList: dict[Optional[Node], int] = {}
        posToNodeMapNewList: dict[int,Optional[Node]] = {}

        curr_ptr = head
        new_head = None
        prev_node = None
        i = 1

        while curr_ptr is not None:
            nodeToPosMapOrigList[curr_ptr] = i
            new_node = Node(curr_ptr.val)
            if prev_node is not None:
                prev_node.next = new_node
            else:
                new_head = new_node
            posToNodeMapNewList[i] = new_node
            i += 1
            prev_node = new_node
            curr_ptr = curr_ptr.next
        
        curr_ptr_orig = head
        curr_ptr_new = new_head

        while curr_ptr_orig is not None:
            if curr_ptr_orig.random is not None:
                randomNodePos = nodeToPosMapOrigList[curr_ptr_orig.random]
                curr_ptr_new.random = posToNodeMapNewList[randomNodePos]
            else:
                curr_ptr_new.random = None
            

            curr_ptr_new = curr_ptr_new.next
            curr_ptr_orig = curr_ptr_orig.next

        return new_head


        