"""
Method 1:
Get the length of longest substring by finding substrings using each of
the element in s as the beginning of a substring. Then, keep the bigger length
between originally kept length and new length.

Time complexity: O(N^2)
Space complexity: O(N)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def substring_length(index):
            substring = set()
            while index < len(s) and s[index] not in substring:
                substring.add(s[index])
                index += 1
            return len(substring)
        
        result = 0
        for i in range(len(s)):
            if substring_length(i) > result:
                result = substring_length(i)
        return result

"""
Method 2:
Use two pointer.

Time complexity:
Space complexity:
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        p2 = 0
        result = 0
        current_length = 0
        string = ''
        while p2 < len(s):
            if s[p2] not in string:
                p2 += 1
            else:
                p1 += 1
            string = s[p1:p2]
            current_length = len(string)
            if current_length > result:
                result = current_length
                
        return result
