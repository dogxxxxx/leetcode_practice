from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {}
        for i, num in enumerate(nums):
            index_dict[num] = i
        
        for i, num in enumerate(nums):
            rest = target - num
            if rest in index_dict and index_dict[rest] != i:
                return [i, index_dict[rest]]
    

if __name__ == "__main__":
    nums = [1,3,4,2]
    target = 6
    result = Solution().twoSum(nums, target)
    print(result)
