from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""Method 1:
Copy a ListNode as head.
Create 2 index to iterate through head and the copy.

Time complexity: O(N), iterating through the head.
Space complexity: O(N), the copy
"""

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        result.next = head
        l = result
        r = head
        while r and r.next:
            if r.next.val != r.val:
                l.next = r
                l = l.next
                r = r.next
            else:
                while r.next and r.next.val == r.val:
                    r = r.next
                r = r.next
        l.next = r
        return result.next