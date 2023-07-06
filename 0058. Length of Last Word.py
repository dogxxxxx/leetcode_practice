"""
Method 1:
No need to explain...

Time complexity: O(N)
Space complexity: O(1)
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

"""
Method 2:
Count the length from behind. This may be faster than method 1.

Time complexity: O(N)
Space complexity: O(1)
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                continue
            else:
                length += 1
                if s[i-1] == " ":
                    break
        return length
