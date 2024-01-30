from typing import List
"""
Method 1:
Two pointer. Need to sort the nums first.

Time complexity: O(N ** 2)
Space complexity: O(1)
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    sums = nums[l] + nums[r] + nums[i]
                    if sums == 0:
                        result.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[l] == result[-1][1]:
                            l += 1
                        while l < r and nums[r] == result[-1][2]:
                            r -= 1
                    elif sums < 0:
                        l += 1
                    else:
                        r -= 1
        return result
    

if __name__ == "__main__":
   nums = [0,0,0,0]
   result = Solution().threeSum(nums)
   print(result)
