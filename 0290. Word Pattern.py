"""
Method 1:
Determine if pattern to s is one to one or not.

Time complexity: O(N) because of s.split
Space complexity: O(N) because of pattern_to_s and s
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        pattern_to_s = zip(pattern, s)
        if len(s) != len(pattern):
            return False
        if len(set(s)) == len(set(pattern)) == len(set(pattern_to_s)):
            return True
        else:
            return False
