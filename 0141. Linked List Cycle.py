# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Method 1:
Keep the ID of each ListNode. If replicated, there is a cycle. Otherwise, there isn't.

Time complexity: O(N)
Space complexity: O(N)
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        id_set = set()
        if not head:
            return False
        while head.next != None:
            if id(head) in id_set:
                return True
            else:
                id_set.add(id(head))
            head = head.next
        return False

"""
Method 2:
The maximum length of the ListNode is 10^4. Thus, if ListNode.next still exists after 10^4 iters, there's a cycle.
This method doesn't work if the maximum length of the ListNode is not given.

Time complexity: O(N)
Space complexity: O(1)
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        i = 0
        while head:
            head = head.next
            i+=1
            if i > 10000:
                return True
        return False

"""
Method 3:
Create a pointer to loop through the ListNode with 2 steps per iteration, while the original head loops with 1 step.
If the IDs of the pointer and the head are the same, there's a cycle.

Time complexity: O(N)
Space complexity: O(1)
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1 = head
        while head and p1 and p1.next:
            p1 = p1.next.next
            head = head.next
            if id(head) == id(p1):
                return True
        return False
