"""
Method 1:
loop through s from the end of s.

Time complexity: O(N)
Space complexity: O(N)
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        result = ''
        last_space = True
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ' and last_space:
                end = i
                last_space = False
                if result:
                    result += ' '
            elif s[i] == ' ':
                if not last_space:
                    result =result + s[i+1:end+1]
                    last_space = True
        if s[0] != ' ':
            result = result + s[i:end+1]
        return result
