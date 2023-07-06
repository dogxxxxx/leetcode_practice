# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Method 1:
Get the length of the linkedlist and find the index of node to be removed from the beginning.
Put the pointer to the index before the index to remove. This method is slow.

Time complexity: O(N)
Space complexity: O(1)
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        length = 0
        pointer = head
        while pointer:
            length += 1
            pointer = pointer.next

        remove_id = length - n
        pointer = head
        for i in range(remove_id - 1):
            pointer  = pointer.next
            
        if n == length:
            head = head.next
        elif pointer.next and pointer.next.next:
            pointer.next = pointer.next.next
        else:
            pointer.next = None
        return head

"""
Method 2:
Create 2 pointers. Move them from beginning and at each step, one of the pointer move n steps.
If it reaches the end, the other pointer's next node is the node to be removed.

Time complexity: O(N)
Space complexity: O(1)
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return
        pointer1 = pointer2 = head
        while True:
            for _ in range(n):
                pointer1 = pointer1.next
            if not pointer1:
                return head.next
            if not pointer1.next:
                pointer2.next = pointer2.next.next
                return head
            pointer2 = pointer2.next
            pointer1 = pointer2
