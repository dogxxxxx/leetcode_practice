"""
Method 1:
Create 2 sets. One for place of departure and the other for destination.
Then, the difference between the 2 sets is the answer.

Time complexity: O(N)
Space complexity: O(N)
"""

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        depart = set()
        dest = set()
        for path in paths:
            depart.add(path[0])
            dest.add(path[1])
        return (dest - depart).pop()
