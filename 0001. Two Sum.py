from typing import List
"""
Method 1:
Use a dictionary to store seen nums with number as key and 
index as value.

Time complexity: O(N)
Space complexity: O(N)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i in  range(len(nums)):
            val = target - nums[i]
            if val in seen:
                return [i, seen[val]]
            else:
                seen[nums[i]] = i
    

if __name__ == "__main__":
    nums = [3,2,4]
    target = 6
    result = Solution().twoSum(nums, target)
    print(result)
