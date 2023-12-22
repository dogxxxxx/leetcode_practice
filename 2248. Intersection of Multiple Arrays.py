from typing import List
"""
Method 1:
Brute force

Time complexity: O(M*N), where M is the length of first list in nums and N is the amount of remaining elements
Space complexity: O(M)
"""

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        result = sorted([x for x in nums[0]])
        for num in nums[0]:
            for i in range(1, len(nums)):
                if num not in nums[i]:
                    result.remove(num)
                    break
        return result


if __name__ == "__main__":
    nums = [[25,44,47,42,43,10],[40,10,8,30,5,23],[36,10]]
    result = Solution().intersection(nums)
    print(result)