from typing import List
"""
Method 1:
Store the amount of each number to a dictionary
Then, convert dict.keys to list and minus 1 to all values.
Do the previous step until the dictionary is empty

Time complexity: O(N**2), while loop is O(N) and list append is O(N)
Space complexity: O(N)
"""

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums_dic = dict()
        for num in nums:
            nums_dic[num] = nums_dic.get(num, 0) + 1
        while nums_dic:
            result.append([x for x in nums_dic.keys()])
            nums_dic = {k: v - 1 for k, v in nums_dic.items() if v > 1}
        return result


if __name__ == "__main__":
    nums = [1,3,4,1,2,3,1]
    result = Solution().findMatrix(nums)
    print(result)