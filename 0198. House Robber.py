from typing import List
"""
Method 1:
DP, memorize full table.

Time complexity: O(N)
Space complexity: O(N)
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        is_steal = [[0, 0] for _ in range(length)]
        is_steal[0] = [0, nums[0]]
        for i in range(1, length):
            is_steal[i][0] = max(is_steal[i - 1])
            is_steal[i][1] = is_steal[i - 1][0] + nums[i]
        return max(is_steal[-1])
    

"""
Method 2:
Memorize previous 2 houses stolen.

Time complexity: O(N)
Space complexity: O(1)
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        curr = nums[0]
        for i in range(1, len(nums)):
            tmp = curr
            curr = max(prev + nums[i], curr)
            prev = tmp
        return curr
    

if __name__ == "__main__":
    nums = [2,7,9,3,1]
    result = Solution().rob(nums)
    print(result)
