"""
Method 1:
No need to consider the length of bin(n)
because the result will be 0 if len(bin(left)) != len(bin(right))
Consider only the same digits from the beginning because if a digit
is not the same, the bitwise and will make them 0.

Time complexity: O(N), where N is the length of the right operand in bits.
Space complexity: O(1)
"""

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        digits = 0
        while left != right:
            left >>= 1
            right >>= 1
            digits += 1
        return left << digits
    

if __name__ == "__main__":
    left = 15
    right = 21
    result = Solution().rangeBitwiseAnd(left, right)
    print(result)