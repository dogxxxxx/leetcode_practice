"""
Method 1:
Compare substring in haystack with needle.

Time complexity: O(N)
Space complexity: O(1)
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
