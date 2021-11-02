# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr = head
        nodes = set()
        while (ptr != None):
            if ptr in nodes:
                return True
            nodes.add(ptr)
            ptr = ptr.next
        return False
        