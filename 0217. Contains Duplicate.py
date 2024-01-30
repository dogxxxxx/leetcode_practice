from typing import List
"""
Method 1:
Compare the length of set and list

Time complexity: O(N)
Space complexity: O(N)
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True

"""
Method 2:
Hash table.

Time complexity: O(N)
Space complexity: O(N)
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False


if __name__ == "__main__":
    nums = [1,2,3,1]
    result = Solution().containsDuplicate(nums)
    print(result)
