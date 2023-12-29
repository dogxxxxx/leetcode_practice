from typing import List
"""
Method 1:
compare the money between robbing
from first house and from second house.

Time complexity: O(N)
Space complexity: O(1)
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev1 = 0
        curr1 = nums[0]
        for i in range(1, len(nums) - 1):
            tmp = curr1
            curr1 = max(prev1 + nums[i], curr1)
            prev1 = tmp
        
        prev2 = 0
        curr2 = nums[1]
        for i in range(2, len(nums)):
            tmp = curr2
            curr2 = max(prev2 + nums[i], curr2)
            prev2 = tmp
        return max(curr1, curr2)
    

if __name__ == "__main__":
    nums = [1,7,9,2]
    result = Solution().rob(nums)
    print(result)