"""
Method 1:
(k==3) = (k<=3) - (k<=2)
Thus, create a function to get (k<=n)
Using sliding windows

Time complexity: O(N)
Space complexity: O(N)
"""

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def lessThanK(nums, k):
            result = 0
            dic = dict()
            l = 0
            for r in range(len(nums)):
                if nums[r] not in dic or dic[nums[r]] == 0:
                    dic[nums[r]] = 1
                    k -= 1
                else:
                    dic[nums[r]] += 1
                while k < 0:
                    dic[nums[l]] -= 1
                    if dic[nums[l]] == 0:
                        k += 1
                    l += 1
                result += r - l + 1
            return result        
        return lessThanK(nums, k) - lessThanK(nums, k - 1)
