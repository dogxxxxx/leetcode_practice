"""
Method 1:
Two pointers

Time complexity: O(N)
Space complexity: O(1)
"""

class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                break
            char = s[left]
            while left <= right and s[right] == char:
                right -= 1
            while left <= right and s[left] == char:
                left += 1

        return right - left + 1
    

if __name__ == "__main__":
    s = "bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"
    result = Solution().minimumLength(s)
    print(result)
