from typing import List
"""
Method 1:
Use dictionary to store the frequency of the nums

Time complexity: O(m+n), m = len(nums), n = len(dict.values())
Space complexity: O(n)
"""

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic = dict()
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1

        max_freq = max(dic.values())
        cnt = 0
        for val in dic.values():
            if val == max_freq:
                cnt += 1

        return cnt * max_freq
    
"""
Method 2:
When updating dictionary, determine if it is
the max freqency at the same time.

Time complexity: O(N)
Space complexity: O(N)
"""

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic = dict()
        max_freq = 0
        cnt = 0
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
            if dic[num] > max_freq:
                max_freq = dic[num]
                cnt = 1
            elif dic[num] == max_freq:
                cnt += 1
        return max_freq * cnt


if __name__ == "__main__":
    nums = [1,2,2,3,1,4]
    result = Solution().maxFrequencyElements(nums)
    print(result)