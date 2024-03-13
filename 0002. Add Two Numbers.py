from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
Method 1:
Create result node from scratch and deal with different situations

Time complexity: O(max(N, M)), where N is len(l1) and M is len(l2)
Space complexity: O(max(N, M))
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False
        result = ListNode(0)
        head = result
        while l1 and l2:
            digit = l1.val + l2.val
            if carry:
                digit += 1
            carry = True if digit >= 10 else False
            node = ListNode(val=digit%10)
            head.next = node
            head = head.next
            l1 = l1.next
            l2 = l2.next

        if not carry:
            head.next = l1 if l1 else l2
        else:
            while l1:
                digit = carry + l1.val
                carry = True if digit >= 10 else False
                head.next = ListNode(val=digit%10)
                head = head.next
                l1 = l1.next
            while l2:
                digit = carry + l2.val
                carry = True if digit >= 10 else False
                head.next = ListNode(val=digit%10)
                head = head.next
                l2 = l2.next
        if carry:
            head.next = ListNode(val=carry)
        return result.next
    